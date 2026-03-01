---
title: "Create your own blog"
subtitle: "GitHub and AWS R53!"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/github.png"
date: 2023-04-21
tags: website create R53 github web page git page
---

## Want to have a bash at creating a blog?

Well, this isn\'t the first time I\'ve thought about creating a blog.

I had previously looked at using [HUGO](https://gohugo.io/). This worked well, and I wrote a few bits but never published them. I just never continued and have since thought about it a number of times.

So this time, as I\'d forgotten what I\'d used last time, I was looking for a static page blog creator. WordPress came up as an option (yeah, slap me). I decided to use AWS and here I started looking at setting up an EC2, R53, EIP, RDS, etc. I wanted to be a smarty‑pants so, stupidly, started writing the Terraform to do this. Advice: that is dumb when you are working out how something is made. Create a POC (proof of concept), get that all working and *then* start writing Terraform.

Whilst looking at an error and creating the repository on Git, I came across [Jekyll](https://jekyllrb.com/). Another learning point is the overwhelming desire to follow a path that you start down. Get out of being precious – you\'re not always right first time.

So I swallowed my pride and started to look at Jekyll. It was so easy: download, execute, and test. Add to that I found that there are loads of themes you can find and these were just as easy – download and you\'re more or less done.

### Simples

So this isn\'t an in‑depth guide but a great starter.  
The Jekyll website has great walkthroughs so I would be doing them an injustice by trying to recreate that, but I will give you the VERY quick and easy way.

Prerequisite: a GitHub account.

1. Hit the [Jekyll Themes website](http://jekyllthemes.org/themes/no-style-please/).
2. Select any theme you fancy.
3. Go to GitHub and create a repository `name.github.io` ([GitHub walkthrough](https://pages.github.com/)).
4. Push the code up to the repo / upload the code manually.
5. Now your website should be up and running.

Well that was easy, wasn\'t it.  
Now, how do we edit this? If you open the `_posts` folder in the code you will see a bunch of test blogs.

The `date` then `name` is advised, e.g. `2023-04-21-name-of-file.markdown`.

You will see that the start/head of the file will contain:

```markdown
***
title: "The Title Which Is Shown On The Main Page"
subtitle: "Sub Title to Title Headline"
author: "You I Guess :D"
avatar: "img/authors/you.jpg"
image: "img/blogimage.png"  # Image shown on the blog icon
date:   1999-01-01          # Date shown on the page 
tags: website R53 github webpage gitpage  # Some tags  \O/
***
