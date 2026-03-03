---
title:  "Auth, OAuth, and JWTs: How They Work — and How Attackers Break Them"
subtitle: "From weak passwords to WebAuthn, with a tour of the common failure modes"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/cards/auth-oauth-and-jwts-how-they-work-and-how-attackers-bre.jpg"
date: 2026-06-07
tags: auth OAuth JWT MFA WebAuthn security attacks
---

## So, What Do We Mean by “Authentication” Anyway?

Authentication is just answering the question: “Who are you, really?” Authorization is the follow‑up: “Now that I know who you are, what are you allowed to do?”

Under the hood, we’ve got multiple mechanisms to prove identity — passwords, tokens, hardware keys, protocols like OAuth and OpenID Connect — each with its own ways of working and its own favourite failure modes.

---

## Weak vs Strong Authentication: How They Work and How They Break

### Weak Auth: Password‑Only and Friends

**How it works (in theory):**

- User types username + password.
- App looks up user, hashes provided password, compares with stored hash.
- If they match, you’re in.

**How it breaks (in reality):**

- **Credential stuffing**: attacker takes leaked email/password combos from breaches and sprays them across sites. Password reuse makes this trivially effective.
- **Brute force**: no rate limiting or lockout → try enough passwords, eventually hit one.
- **Phishing**: fake login pages (often pixel‑perfect clones) capture credentials and replay them on the real site.
- **Password reset abuse**:
  - Weak “security questions” easily OSINT’d.
  - Token links that never expire or are guessable.

Once you’ve got password‑only auth with no extra checks, an attacker with a laptop and some patience has everything they need.

---

### MFA and 2FA: Extra Factors, New Attack Surfaces

**How it works:**

- You prove *something you know* (password).
- Plus *something you have* (phone, app, hardware key) or *something you are* (biometric).
- Common methods:
  - TOTP codes (Authenticator apps).
  - SMS codes.
  - Push prompts (“Approve sign‑in?”).
  - WebAuthn/FIDO2 security keys.

**How it breaks:**

- **SMS codes**:
  - SIM swap / port‑out attacks.
  - Interception via SS7 flaws.
- **TOTP codes**:
  - Phishing proxies: real‑time relays capture both password and code, log in immediately before expiry.
- **Push MFA**:
  - MFA fatigue: spam the user with prompts until they hit “Approve” just to make it stop.
- **Device theft**:
  - If the device is unlocked and the app auto‑approves/auto‑fills, it’s game on.

So MFA is *much* better than password‑only, but anything that still relies on the user making a good decision on a fake login page can be bypassed.

---

### WebAuthn / FIDO2: How Strong Auth Actually Works

**How it works:**

- During registration:
  - Your browser and authenticator (security key, TPM, phone) generate a unique key pair per site.
  - Public key goes to the server; private key never leaves the device.
- During login:
  - Server sends a challenge bound to the real origin (domain).
  - Device signs the challenge with the private key *only if* the origin matches and you confirm (touch key, biometric, PIN).
  - Server verifies signature with stored public key.

**Why it’s hard to break:**

- Phishing site at `evil-login.com` presents a challenge, but the authenticator sees the wrong origin and refuses to sign with the key tied to `real-site.com`.
- No shared secret to steal or replay; credentials are per‑site and hardware‑bound.
- Even backend credential dumps don’t reveal a secret that can log in directly (public keys are… public).

**How attackers try anyway:**

- Go after device/OS compromise to hijack the authenticator.
- Social engineering + remote access (get the user to “approve” while attacker drives).
- Target fallback/recovery flows (password resets, backup codes).

---

## OAuth 2.0 and OpenID Connect: How They Work and How They Break

### OAuth 2.0: Delegated Access, Not “Login”

**How it works (Authorization Code + PKCE):**

1. Your app redirects the user to the IdP (e.g. `https://idp.com/authorize`) with:
   - client_id, redirect_uri, scopes, state, code_challenge.
2. User logs in at IdP, consents.
3. IdP redirects back with an authorization code and the original state.
4. Your backend exchanges the code + code_verifier for tokens at the IdP’s token endpoint.
5. App uses access token to call APIs on behalf of the user.

PKCE protects against code interception by binding the code to a verifier only the client knows.

**How it breaks:**

- **Wrong grant for the job**:
  - Using Implicit flow → tokens in the URL fragment, vulnerable to interception and XSS.
  - Using ROPC → your app collects passwords directly, breaking isolation and increasing phishing risk.
- **Open redirect / redirect_uri poisoning**:
  - If `redirect_uri` isn’t strictly validated, an attacker can get codes or tokens sent to their domain.
- **Missing state checks**:
  - CSRF in the login flow; an attacker can log a victim into a session tied to the attacker’s account (session fixation).
- **Token theft and replay**:
  - Access tokens stored insecurely on the client (e.g. in localStorage), stolen via XSS.

---

### OpenID Connect: Identity on Top of OAuth

**How it works:**

- Same OAuth dance, but with the `openid` scope.
- IdP returns:
  - Access token (for calling APIs).
  - ID token (usually a JWT) describing the authenticated user.
- The client validates the ID token (issuer, audience, signature, expiry) and treats that as proof of identity.

**How it breaks:**

- **Not validating ID token fields**:
  - Accepting any issuer or audience → attacker can present an ID token from another tenant or IdP.
- **Leaking ID tokens**:
  - Storing them where JavaScript/XSS can grab them (localStorage, query params).
- **Mix‑up attacks**:
  - Poorly implemented clients confused about which IdP a response came from.

Done properly, OIDC saves you from rolling your own auth. Done badly, it gives you a fancy way to accept unverified blobs as “logged‑in user.”

---

## JWTs: How They Work and How Attackers Abuse Them

### How JWTs Work

A JSON Web Token is three base64url‑encoded parts: `header.payload.signature`.

- Header:
  - `alg`: algorithm (e.g. HS256, RS256).
  - `typ`: usually `JWT`.
- Payload:
  - Claims: `sub`, `iss`, `aud`, `exp`, roles, etc.
- Signature:
  - HMAC (HS*) or asymmetric signing (RS*, ES*).

Verification flow:

1. Decode header and payload.
2. Look up the right key based on header/kid.
3. Check algorithm is allowed.
4. Verify signature.
5. Validate claims (issuer, audience, expiry, etc.).

### How JWTs Get Broken

Classic attacks:

- **`alg: none` / algorithm confusion**:
  - Old/bad libraries: if header says `alg: none`, they skip signature verification.
  - HS ↔ RS confusion:
    - If server expects RS256 but treats key as HMAC, attacker signs with the public key as if it were a shared secret.

- **Key guessing and weak secrets**:
  - HS256 with a short secret (e.g. “secret”, project name) → brute forceable.

- **Ignoring critical claims**:
  - Not checking `exp` → token valid forever.
  - Not checking `aud` → token for Service A accepted by Service B.
  - Not checking `iss` → token from attacker‑controlled IdP accepted as if from your own.

- **Storing JWTs in all the wrong places**:
  - `localStorage` → stolen via XSS.
  - Query string → leaks in logs, referrers.

- **Shoving sensitive data inside**:
  - JWTs are signed, not encrypted; payloads are easily decodable.
  - Storing passwords, secrets, or unnecessary PII in tokens leaks that data to anyone who can see the token.

Mitigations: strong keys, short expiries, strict algorithm and claim checks, and only putting what you *actually* need in the token.

---

## Sessions vs Token‑Based Auth: Workflows and Attack Surfaces

### Traditional Cookie‑Based Sessions

**How it works:**

- After login, server creates a session entry in a DB/cache keyed by a random ID.
- Client gets an `HttpOnly`, `Secure` cookie with that session ID.
- On each request, server looks up session, applies authz.

**Common attacks:**

- **Session fixation**:
  - Attacker sets a known session ID for victim, then uses it later.
- **Session hijacking**:
  - Steal cookie via XSS, insecure transport (no HTTPS), or theft of machine.
- **CSRF**:
  - Browser automatically attaches cookies → drive the victim’s browser to send authenticated requests they didn’t intend.

Mitigations: secure flags on cookies, CSRF tokens, same‑site cookies, rotation of session IDs after login, short idle timeouts.

### Token‑Based (JWT) Auth

**How it works:**

- After login or OAuth flow, client receives access token (JWT).
- Client sends token in `Authorization: Bearer` header to APIs.
- Server verifies token signature and claims, no session DB needed.

**Common attacks:**

- **XSS token theft**:
  - If token is stored in JS‑accessible storage.
- **Replay**:
  - Stolen token used from another device/IP until expiry.
- **Misconfigured validation**:
  - All the JWT issues we discussed above.

Mitigations: store tokens in HttpOnly cookies or secure storage, short TTLs + rotation, strict JWT validation, TLS everywhere.

---

## Putting It All Together: How to Build and How to Break (In a Lab)

### A Modern Strong Auth Flow (Build This)

- Use **OIDC** with Authorization Code + PKCE.
- Back it with:
  - Password + TOTP MFA as minimum.
  - WebAuthn/FIDO2 for admins/high‑risk roles and eventually everyone.
- Use:
  - Short‑lived access tokens (JWTs or opaque).
  - ID tokens only on the client; don’t spray them at every backend.
- Validate tokens:
  - Signature, algorithm, issuer, audience, expiry, nonce where relevant.
- Stick to secure storage:
  - HttpOnly cookies or secure token stores, not localStorage.

### How to “Red Team” It (Safely)

In a lab or test environment, practise:

- Building a fake login page and seeing which methods are phishable (password, TOTP, push) and which aren’t (WebAuthn).
- Attempting:
  - Token replay (reusing captured access tokens).
  - Modifying JWT headers/payloads to see if validation catches it (e.g. changing `alg`, `aud`, or `exp`).
  - CSRF against cookie‑based flows without CSRF protections.
- Reviewing:
  - If fallback flows (password reset, backup codes, device “remember me”) are weaker than the main auth path.

The goal isn’t just to break things; it’s to understand *exactly why* they broke and how to defend against those routes.

---

## Final Thought

Auth is where attackers go first because it’s where “outside” meets “inside.” Understanding how these mechanisms work — and exactly how they’re commonly broken — is what separates “we implemented OAuth” from “we actually have a robust, testable, and defendable authentication story.”

Design for strong auth from day one. Then, in the lab, learn to break your own designs. The real win is when those lessons make it into the next system you build.

<img src="img/authors/geeky.jpg" width="40"/>