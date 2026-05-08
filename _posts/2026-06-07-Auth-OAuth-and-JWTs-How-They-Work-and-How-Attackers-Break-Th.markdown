---
title:  "Auth, OAuth, and JWTs: How They Work — and How Attackers Break Them"
subtitle: "From weak passwords to WebAuthn, with a tour of the common failure modes"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/auth-oauth-and-jwts-how-they-work-and-how-attackers-bre.jpg"
date: 2026-06-07
tags: auth OAuth JWT MFA WebAuthn security attacks
---

## So, What Do We Mean by "Authentication" Anyway?

Authentication is just answering "who are you, really?" Authorization is the follow-up: "now that I know who you are, what are you allowed to do?" Most security incidents I've helped clean up live somewhere in that gap — the bit between "I logged in" and "the system trusts me to do this thing".

Under the hood we have multiple mechanisms — passwords, tokens, hardware keys, protocols like OAuth and OpenID Connect. This post is the working tour: how each works, the canonical failure modes with attack examples you can run in a lab, and the fixes you should be writing into your codebase. For the broader architecture this fits into, see [Zero Trust Architecture: A Deep Practical Walkthrough](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough).

---

## Weak vs Strong Authentication

### Password-Only and Friends

**How it works (in theory):** user types username and password; app hashes input and compares with stored hash; match means in.

**How it breaks (in reality):**

- **Credential stuffing.** Leaked email/password combos from breaches sprayed across sites. Password reuse makes this trivially effective.
- **Brute force.** No rate-limit or lockout → throw passwords until one lands.
- **Phishing.** Pixel-perfect clone login pages capture credentials and replay them.
- **Password reset abuse.** Weak security questions are OSINT-able. Reset tokens that don't expire or are guessable. Race conditions in the reset endpoint.

If your auth is password-only with no extra checks, an attacker with patience and a list has everything they need.

### MFA / 2FA

**How it works:** prove *something you know* (password) plus *something you have* (phone, app, hardware key) or *something you are* (biometric).

**How it breaks:**

- **SMS codes** — SIM-swap or port-out attacks; SS7 interception still happens in 2026 despite years of patching.
- **TOTP (Authenticator app codes)** — phishing proxies (evilginx2, modlishka) capture the password and the code in real time and log in immediately. The user thinks they typed it into the real site.
- **Push MFA fatigue** — spam the user with prompts at 2am until they tap "Approve" to make it stop. The Uber 2022 breach started this way.
- **Number-matching push** — better than vanilla push, still phishable when the attacker is in the loop.
- **Device theft with unlocked screens** — auto-fill, auto-approve.

MFA is much better than password-only, but anything that relies on the user making a good decision on a fake page can be bypassed.

### WebAuthn / FIDO2 / Passkeys: Strong Auth That Actually Holds

**How it works:**

- During registration, your browser and authenticator (YubiKey, TPM, phone Secure Enclave) generate a unique key pair *per origin*. The public key is stored on the server; the private key never leaves the device.
- During login, the server sends a challenge bound to the real origin. The device signs the challenge only if the origin matches and you confirm (touch, biometric, PIN).
- The server verifies the signature with the stored public key.

**Why it’s phishing-resistant:**

- A phishing site at `evil-login.com` presents a challenge, but the authenticator sees the wrong origin and refuses to sign with the key tied to `real-site.com`. There's no shared secret to steal.
- Credential dumps don't reveal anything that can log in directly — public keys are public.

A minimal Node/Express WebAuthn registration using the well-maintained `@simplewebauthn/server` library:

```javascript
import {
  generateRegistrationOptions,
  verifyRegistrationResponse,
} from '@simplewebauthn/server';

// Step 1 — server prepares challenge for browser
app.get('/webauthn/register/options', async (req, res) => {
  const user = req.session.user;
  const options = await generateRegistrationOptions({
    rpName: 'Geeky Blinder Auth Demo',
    rpID: 'auth.example.com',          // bound to the real origin
    userID: Buffer.from(user.id),
    userName: user.email,
    attestationType: 'none',
    authenticatorSelection: {
      residentKey: 'preferred',
      userVerification: 'preferred',
      authenticatorAttachment: 'platform', // or 'cross-platform' for keys
    },
    timeout: 60_000,
  });
  req.session.currentChallenge = options.challenge;
  res.json(options);
});

// Step 2 — server verifies what the browser returns
app.post('/webauthn/register/verify', async (req, res) => {
  const { credential } = req.body;
  const expectedChallenge = req.session.currentChallenge;

  const verification = await verifyRegistrationResponse({
    response: credential,
    expectedChallenge,
    expectedOrigin: 'https://auth.example.com',
    expectedRPID: 'auth.example.com',
  });

  if (!verification.verified) return res.status(400).json({ error: 'verify failed' });

  await db.credentials.insert({
    userId: req.session.user.id,
    credentialID: verification.registrationInfo.credentialID,
    publicKey: verification.registrationInfo.credentialPublicKey,
    counter: verification.registrationInfo.counter,
  });

  res.json({ ok: true });
});
```

The key thing to notice: `expectedOrigin` and `expectedRPID` are pinned server-side. Even if a phishing page collects the response, the verification fails because the origin doesn’t match.

**How attackers still try:**

- Compromise the device or OS to hijack the authenticator.
- Social engineering plus remote access — get the user to "approve" a real challenge while the attacker drives the session.
- Target fallback flows (password reset, backup codes, recovery contacts) that often aren't WebAuthn-protected.

The lesson: roll out WebAuthn aggressively, but harden the recovery paths the same way.

---

## OAuth 2.0 and OpenID Connect

### OAuth 2.0: Delegated Access, Not "Login"

**How it works (Authorization Code + PKCE — the only flow you should be using in 2026):**

1. Your app redirects to the IdP with `client_id`, `redirect_uri`, `scope`, `state`, `code_challenge`.
2. User logs in at the IdP, consents.
3. IdP redirects back with an authorization code + the original `state`.
4. Your backend exchanges the code + `code_verifier` for tokens at the IdP's token endpoint.
5. App uses access token to call APIs.

PKCE binds the code to a verifier only the client knows, so even if the code leaks, it can't be exchanged.

**How it breaks:**

- **Wrong grant type.** Implicit flow puts tokens in the URL fragment — interceptable, leakable through Referer headers, broken. ROPC (Resource Owner Password Credentials) makes your app collect passwords directly, killing the whole "delegated" point. Both deprecated by OAuth 2.1; if you're still using either, that's the bug.
- **Open redirect / `redirect_uri` poisoning.** If the IdP doesn't strictly validate `redirect_uri` against a registered list, an attacker can get codes sent to their domain. Use exact-match registered URIs, never wildcards.
- **Missing `state` checks.** CSRF in the login flow; an attacker can log a victim into the *attacker's* session (session-fixation-shaped). Always verify `state` round-trips correctly.
- **Token theft via XSS.** Access tokens in `localStorage` are stealable by any script on the page. Use `HttpOnly` cookies or [BFF (Backend-For-Frontend) pattern](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps).
- **Refresh token abuse.** Long-lived refresh tokens stored insecurely become master keys. Rotate them on every use and detect reuse.

### OpenID Connect: Identity on Top of OAuth

**How it works:** same OAuth dance with the `openid` scope. The IdP returns an *ID token* (a JWT) describing the authenticated user. Your client validates it (issuer, audience, signature, expiry, nonce) and treats that as proof of identity.

**How it breaks:**

- **Not validating ID-token fields.** Accepting any `iss` or `aud` → an attacker can present an ID token from another tenant or IdP and your app accepts it as "logged in".
- **Leaking ID tokens** — `localStorage`, query strings, server logs, browser history.
- **Mix-up attacks** — clients confused about which IdP a response came from when supporting multiple IdPs.
- **Nonce missing or unchecked** — replay attacks on ID tokens.

Done properly, OIDC saves you from rolling your own auth. Done badly, it's a fancy way to accept unverified blobs as "logged-in user".

---

## JWTs: The Three-Part Token, and the Three-Part Disaster

A JSON Web Token is three base64url-encoded parts: `header.payload.signature`.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9      ← header
.eyJzdWIiOiIxMjM0Iiwicm9sZSI6InVzZXIifQ   ← payload
.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQ   ← signature
```

**Header** has `alg` (algorithm) and `typ`. **Payload** has claims (`sub`, `iss`, `aud`, `exp`, custom). **Signature** is HMAC (HS*) or asymmetric (RS*, ES*, EdDSA).

### The Right Way to Verify

A correct JWT verification checks signature, algorithm, issuer, audience, and expiry. The *common* failure is to verify the signature only.

```python
import jwt
from jwt import PyJWKClient

JWKS_URL  = "https://idp.example.com/.well-known/jwks.json"
ISSUER    = "https://idp.example.com/"
AUDIENCE  = "https://api.example.com/"
ALGORITHMS = ["RS256"]   # ALLOWLIST — never read alg from the token alone

jwks_client = PyJWKClient(JWKS_URL)

def verify(token: str) -> dict:
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    return jwt.decode(
        token,
        signing_key.key,
        algorithms=ALGORITHMS,        # explicit
        audience=AUDIENCE,            # checked
        issuer=ISSUER,                # checked
        options={"require": ["exp", "iat", "iss", "aud", "sub"]},
    )
```

The two non-obvious lines: `algorithms=["RS256"]` is an allowlist, not a hint — never trust the `alg` field in the token. `options.require` forces expected claims to be present, so a token missing `exp` doesn't get accepted as "expires never".

### How JWTs Get Broken — With Lab Examples

Set up a deliberately bad verifier in a lab and run these against it.

**`alg: none` bypass.** Some old libraries (or hand-rolled "verifiers") will accept `alg: none` and skip signature verification:

```python
import jwt

# Forge a token that claims admin role with no signature
forged = jwt.encode({"sub": "1234", "role": "admin"}, "", algorithm="none")
print(forged)
# Send this in Authorization: Bearer <forged>
```

If your verifier accepts it, you've got the bug. The fix is the allowlist above (`algorithms=["RS256"]`) — `none` will never be in it.

**HS / RS algorithm confusion.** If the server expects RS256 (asymmetric) but the verifier code reads `alg` from the token and just uses "the key", an attacker can flip to HS256 and sign with the public key as if it were an HMAC secret:

```python
import jwt

# attacker has the server's public key (it's public!)
with open("server-pub.pem") as f:
    pubkey = f.read()

forged = jwt.encode({"sub": "victim", "role": "admin"}, pubkey, algorithm="HS256")
# Some verifiers do `jwt.decode(token, pubkey)` without algorithm pinning → bypass
```

**Weak HMAC secret.** HS256 with a short secret like `"secret"`, your project name, or `"changeme"` is brute-forceable in seconds with `hashcat` or `jwt_tool`:

```bash
# given a captured token in token.txt
hashcat -a 0 -m 16500 token.txt /usr/share/wordlists/rockyou.txt
```

If your secret cracks, rotate immediately and audit every place you accepted that token.

**Ignoring critical claims.** No `exp` check → token valid forever. No `aud` check → a token issued for service A is accepted by service B. No `iss` check → a token from an attacker's IdP is accepted as if from yours.

```bash
# Curl test for missing exp check — strip exp from a token, replay
python3 -c "import jwt; print(jwt.encode({'sub':'1234','role':'admin'}, 'KEY', algorithm='HS256'))"
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/admin/users
```

**Storing JWTs in the wrong place.** `localStorage` is XSS-stealable. Query strings end up in logs, referrers, and bookmarks. Use HttpOnly secure cookies, or a BFF that holds the token server-side and gives the browser a session cookie.

**Putting sensitive data in the JWT body.** JWTs are signed, not encrypted. Anyone with the token can decode the payload. Don't put passwords, secrets, full PII, or anything you wouldn't print on a postcard. If you need confidential claims, use [JWE (JSON Web Encryption)](https://datatracker.ietf.org/doc/html/rfc7516) or look up the data server-side from an opaque token.

---

## Sessions vs Token-Based Auth

### Cookie-Based Sessions (The Boring Reliable Default)

Server creates a session keyed by random ID, stores in DB/cache, sends `HttpOnly Secure SameSite=Lax` cookie to the client. Each request, server looks up the session.

**Common attacks:**

- **Session fixation** — attacker plants a known session ID for the victim, hijacks once they log in. Mitigation: rotate the session ID on login.
- **Session hijacking** — cookie stolen via XSS or insecure transport. Mitigation: `HttpOnly`, `Secure`, `SameSite=Lax/Strict`, TLS everywhere.
- **CSRF** — browser auto-attaches cookies. Mitigation: `SameSite=Lax` covers most cases; CSRF tokens or double-submit cookies for state-changing endpoints.

Boring, works, well-understood. Most of the post is about "the new ways" but the old way is fine for many apps.

### Token-Based (JWT in `Authorization: Bearer`)

Server returns a token (often JWT) on login. Client sends in `Authorization: Bearer <token>` per request. Stateless on the server side.

**Common attacks:** all the JWT misconfigurations above, plus storage issues (XSS-stealable storage), plus replay (stolen token used until expiry).

**Mitigations:** strict JWT validation as in the verifier above, short access-token TTLs (5–15 minutes) with refresh-token rotation, secure storage (HttpOnly cookies via BFF or hardware-bound), TLS everywhere.

The 2026 guidance is: prefer the BFF pattern for browser SPAs (server holds the token, browser holds a session cookie); use JWTs in the `Authorization: Bearer` header for service-to-service and mobile apps.

---

## Authorization: A Quick Aside

Authentication ("are you Bob?") is answered above. Authorization ("can Bob delete this?") is a separate problem. Two patterns worth knowing:

**Tokens with claims** — JWT contains `roles`, `groups`, or scoped permissions. App reads them and decides. Fast, but tokens go stale and you're trusting whatever was true when the token was issued.

**Policy engine** — [OPA](https://www.openpolicyagent.org/) or [AWS Cedar](https://www.cedarpolicy.com/) evaluates each access decision against current state. Slower per-request, but real-time and centrally auditable. Worth it for anything sensitive.

A minimal OPA rego policy enforcing "admins can do anything; users can only edit their own resources":

```rego
package authz

default allow := false

allow if {
    input.user.role == "admin"
}

allow if {
    input.user.role == "user"
    input.action in {"read", "update"}
    input.resource.owner_id == input.user.id
}
```

Combine policy decisions with telemetry so every "allow" and every "deny" is logged. The "every deny" part catches reconnaissance.

---

## A Modern Strong Auth Stack (Build This)

- **OIDC** with Authorization Code + PKCE for user auth.
- **WebAuthn / passkeys** for the primary factor where supported; password + TOTP as fallback for users who can't or won't use passkeys yet.
- **Phishing-resistant MFA** for admins and high-risk roles, full stop.
- **Short access tokens** (5–15 min) + rotating refresh tokens with reuse detection.
- **JWT verification** with explicit algorithm allowlist and required claims (the Python snippet above is the shape).
- **Tokens in HttpOnly cookies** via BFF for browser SPAs; `Authorization: Bearer` for service-to-service.
- **Authorization via policy engine** for non-trivial decisions; tokens for hot-path checks.
- **Logging on every deny** and every fallback flow. The recovery paths are where attackers go when the front door is locked.

---

## How to Red-Team This Safely

In a lab or against your own staging environment:

- **Stand up evilginx2 or modlishka** against a fake login page with TOTP. Confirm WebAuthn-protected accounts can't be phished.
- **Replay captured access tokens** from another browser/IP after the user logs out. Should fail; if it works, your TTL is too long or your revocation is broken.
- **Modify JWT headers and payloads.** Try `alg: none`, change `aud`, change `exp`, change `role`. Each one should be rejected with a specific error.
- **Hit endpoints without `state`** in the OAuth flow. Confirm it's rejected.
- **Test the recovery paths.** Password reset, backup codes, "remember this device" flows. The bypass is usually here.
- **Check open redirects** on `redirect_uri` and post-login destination.

The goal isn't just to break things; it's to understand exactly *why* they broke and how to defend the path. Each finding becomes a regression test.

---

## Final Thought

Auth is where attackers go first because it’s where "outside" meets "inside". Understanding how these mechanisms work — and how they’re commonly broken — is what separates "we implemented OAuth" from "we have a robust, testable, defendable authentication story".

Design for strong auth from day one, then in the lab learn to break your own designs. The real win is when those lessons make it into the next system you build, the runbook your on-call follows, and the test suite that catches regressions before users notice.

For the architecture this lives inside, see [Zero Trust Architecture](https://geekyblinder.co.uk/#/2026/05/10/Zero-Trust-Architecture-A-Deep-Practical-Walkthrough). For the human side, [Password Managers](https://geekyblinder.co.uk/#/2026/02/15/Password-Managers).

<img src="img/authors/geeky.jpg" width="40"/>
