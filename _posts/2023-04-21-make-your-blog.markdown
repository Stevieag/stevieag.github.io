---
title: "Create your own Blog"
subtitle: "Github and AWS R53!"
author: "Geeky Blinder"
avatar: "img/authors/geeky.jpg"
image: "img/github.png"
date: 2023-04-21
tags: website create R53 github web page git page
---

## Want to have a bash at creating a blog?


Well, this isn't the first time ive thought about creating a blog.


I had previously looked at using [HUGO](https://gohugo.io/). This worked well, and i wrote a few bits but never published this. I just never continued and have since thought about it a number of time.

So this time I, as id forgotten what id used last time, I was looking for a static page blog creator. WordPress came up as an option (Yeah, slap me). I decided to use AWS and here i started looking at setting up an EC2, R53, EIP, RDS etc... I Wanted to be a smarty-pants so , stupidly started writing the terraform to do this. Advise, that is dumb when you are working out how something is made. Create a POC (proof of concept), get that all working and _then_ start writing terraform.

Whilst looking at an error and creating the repository on git, I came across [Jekyll](https://jekyllrb.com/). Another learning point is the overwhelming desire to follow a path that you start down. Get out of being precious, you're not always right first time.

So I swallowed my pride and started to look at Jekyll. It was so easy, download, execute and test. Add to that I found that there are loads of themes you can find and these were just as easy, download and you're more or less done.

### Simples

So this isn't an in depth guide but a great starter.
Jekyll website has great walkthroughs so i would be doing them an injustice by trying to recreate that but i will give you the VERY quick and easy way. Prerequisite : a GitHub account
1. Hit [Jekyll Themes website](http://jekyllthemes.org/themes/no-style-please/)
2. Select any theme you fancy
3. Go to GitHub and create a repository names.github.io [{GitHub Walkthrough}](https://pages.github.com/)
4. Push the code up to the repo/upload the code manually
5. Now your website should be up and running.

Well that was easy wasn't it.
Now how do we edit this. If you open the _posts folder in the code you will see a bunch of test blogs.

The 'date' then 'name' is advised, eg 2023-04-31-name-of-file.markdown.

You will see that the start/head of the file will contain:
```markdown
    ---
    title: "The Title Which Is Shown On The Main Page"
    subtitle: "Sub Title to Title Headline"
    author: "You I Guess :D"
    avatar: "img/authors/you.jpg"
    image: "img/blogimage.png" <<<< Image shown on the blog icon
    date:   1999-01-01 <<<< Date shown on the page 
    tags: website R53 github webpage gitpage <<<<< Some tags  \O/
    ---
```
The date is when the file will be shown. So you could push this file earlier and it will be hidden until that date. I wouldnt rely on it as i havnt checked if its taken from client or server but it is interesting and it does seem to work.

As you can see the page is in markdown and can be created with quick formatting. A good starter is [rip tutorial](https://riptutorial.com/markdown) or ideal is [GitHubs markdown instructions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)

Some folders may be different and need creating dependent on the theme you use. In my case I needed extra folders creating.

So this is the quick fire, whizz through to get a basic site up.
Next we will follow through with a slightly deeper walkthrough. In this we will set up Jekyll on our machine and run this locally, so we can see immediate changes before upload.

### Jekyll

Stolen from [jekylls site](http://jekyllrb.com/)

```
~ $ gem install bundler jekyll
~ $ jekyll new my-awesome-site
~ $ cd my-awesome-site
~ $ bundle exec jekyll serve
# => Now browse to http://localhost:4000 
```
There you go, its running local on your machine.....

Weeeelllll, it wasn't that simple for me.
First, Jekyll requires the following:

 Ruby version 2.5.0 or higher
 RubyGems
 GCC and Make

So off I go to install these. I was running PopOS (Ubuntu)
So, [requirements page](http://jekyllrb.com/docs/installation/#requirements)
I installed all according to the instructions for Ubuntu. Now I owe you an apology. I had issues and I didnt document them to place here but suffice to say it was painful to get to run. I did a bit of googling on the error that the installed tool was not found and fixed it... sorry.

Once installed it is as easy as running as above `Jekyll new my-site`
Then cd to the new folder named `ny-site` and run `bundle exec Jekyll serve`
If you then open your browser and type in `http://localhost:4000` or `127.0.0.1:4000` - you should see your new site. (You may get a warning that you site is insecure, dont worry and bypass this, it is due to no ssl certificate but we trust ourself and its local only (no outside world). If you are worried you can pass your code through [VirusTotal](https://www.virustotal.com/))

You can edit as instructed and each new update will automagically be seen in your browser.

When you have finished, input `Ctrl c` to stop the server.
When you are happy you can push the changes to GitHub as normal, give it a couple of minutes and POW, new site update.

Wait.... One good thing now that you have Jekyll install is that you can check out the themed site we made earlier.
`cd` to the theme folder, in here run `Jekyll serve` and now in your browser you can assess the themed version of a site that you can adapt to suite.


### Your URL

Lastly we will set up a URL of our own using AWS and Route 53.
Well, this was my real goal unless you chose a great GiHub name or it is your name and you used as a CV. No point having a site named hairymary6767.github.io!!.

So your gonna need an AWS account. If you dont have one, well off you go and get one. Theres a lot of free stuff for you to play with and learn. Im new to this so ive looked at my AWS and id say it will cost no more than £10. 
I have two urls and a bunch of other stuff and my bill is £11 - I'll update this if it changes significantly.

1. In your repository, create a file (no need for an extension).In this file add your url eg `geekyblinder.co.uk`
2. git add this file ( `git add . && git commit -m 'CNAME record' && git push` )
3. Now we can configure our R53
    - 3a. Log into the AWS console
    - 3b. Click onto the Route 53 dashboard
    - 3c. Click on Hosted zones
    - 3d. Click on the domain you are using
    - 3e. Click Create Record
    - 3f. Ignore the Name field
    - 3g. Under the Type dropdown, select `A` record
    - 3h. Set Alias toggle to `No`
    - 3i. Enter into the text area the IPs 
    ```
        185.199.108.153 
        185.199.109.153 
        185.199.110.153 
        185.199.111.153
    ```
    - 3j. Click Save Record Set.
4. Click on create Record again
    - 4a. In the Name field enter `www`
    - 4b. Under Type select `A`
    - 4c. Set Alias toggle to `Yes`
    - 4d. In the Alias field, select the domain we previously set up eg `geekyblinder.co.uk`
    - 4e. Save the Record
5. Now configure GitHub page to use you URL
    - 5a. On your GitHub account and then the settings tab
    - 5b. Go to the GitHub Pages section
    - 5c. In custom domain, enter your domain: geekyblinder.co.uk
    - 5d. Now verify the URL by adding some DNS TXT records
        - 5da. Go to AWS R53 and create a new record.
        - 5db. Create a TXT record in your DNS
        - 5dc. Add hostname `_github-pages-challenge-yourgit``.yoururl.com`
        - 5dd. Add the provided code eg `12a3b4567cdef8901g234h567890123` for the value of the TXT record.
        - 5de. Wait until your DNS configuration changes.
            -  This could take up to 24 hours to propagate is the warning you will see but its usually minutes.
            - You can exit and come back to verify by the use of the three dots against the name
        <center><img alt="github challenge record" src="img/githubrecordchallenge.png" width="340"/></center>
        - 5df. Click verify
6. Now it may take a little time for the records to propogate
7. Now check that the `https://` and `http://` versions of your site are now working plus then with and without `www.`
    eg  
    - [https://geekyblinder.co.uk](https://geekyblinder.co.uk)
    - [http://geekyblinder.co.uk](http://geekyblinder.co.uk)
    - [https://www.geekyblinder.co.uk](https://www.geekyblinder.co.uk)
    - [http://www.geekyblinder.co.uk](http://www.geekyblinder.co.uk)

BTW - its set to forward `http` to `https`

<img src="img/authors/geeky.jpg" width="40"/>