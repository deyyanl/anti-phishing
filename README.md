# Sending spam to phishing websites with Python

## How I got the idea
In my spam mail box, I got this mail
![Mail](https://cdn.obrn.space/files/eq7z9.png)

So, I wanted to play with the guy(s) behind the page, and this is the result :)

## Network analysis
We need to do network analysis to see where the site sends form data.
- Open **Chrome DevTools** (or your browser's equivalent) after the page loads (to get rid of extra unnecessary data)
- Select **Preserve logs**

![Network](https://cdn.obrn.space/files/br591.png)


Then, enter test data in the form (e.g. bla:bla)

![Example](https://cdn.obrn.space/files/wzzrx.png)

After that, proceed with the "login" and monitor the network capture.

## Network capture
Bam, we got a lot of data!

![Data](https://cdn.obrn.space/files/lqp27.png)

Now, this will be different for you, but this guy (someone who made this) uses **attempts.php** to see how many tries have you made, and
send in plain text your data over **POST** request. (insert facepalm here). 

This is the URL that we want, the URL which gets our data.

![Example2](https://cdn.obrn.space/files/2npn5.png)

As we scroll down, we will find **Form data**, here we will choose the source of data that has been sent.

![Example3](https://cdn.obrn.space/files/37sgk.png)

![Example4](https://cdn.obrn.space/files/z2vnh.png)

So now we know what data we need to send using **POST** request. We'll send it as a plain text like he does.

What this guy does, is that it logs you into your private repositories using GitHub's API for that, while doing that they are stealing your credentials, as we saw
that from the network analysis, when you log in, only security vulnerability you will find is that they're stealing your data.

# Dependecies
- [lxml](https://lxml.de)
- [requests]

## Credits
- [deyyanl](https://github.com/deyyanl)
- [Minlor](https://github.com/Minlor)