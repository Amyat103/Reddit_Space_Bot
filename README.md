# Reddit Space Picture Bot
Reddit Bot built with Python and PRAW <br> This program will post NASA's APOD(Astronomy Picture of the Day) at 12 p.m. each day and will post 3 random APODs at 5 p.m. each day. The pictures are requested from NASA's API. The requested pictures are downloaded, posted and immediately deleted after posting so no space is required.
This program is built following the PRAW documentation(https://praw.readthedocs.io/en/stable/index.html) <br>
the purpose of this bot is to post and share space-related pictures <br>

## Why I Built This Bot
I've always been interested in space and love looking at pictures and articles about it. Making this bot that posts a space picture and has an explanation on the bottom is a way to share my interest with like-minded people since this is posted only in a subreddit about space.

### Installing PRAW and Requests

These are the libraries you'll need

```
pip install praw
pip install requests
```

## Deployment
This bot is currently deployed on Python Anytime (www.pythonanywhere.com)

Example:
With these lines inside main(), the program will check every 40 sec if it's time to execute the 4 functions that runs this bot
```
def main():
    print("BOT STARTED")
    # daily single post
    schedule.every().day.at("12:00").do(reddit_post_daily)

    # deleting the image after posting
    schedule.every().day.at("12:02").do(remove_pic)

    # daily gallery post
    schedule.every().day.at("17:00").do(reddit_post_rand)

    # deleting the image after posting
    schedule.every().day.at("17:02").do(remove_gal)


    while True:
        schedule.run_pending()
        time.sleep(40)
```
<br>

## Example
### This is an example of Daily APOD Post, the bot will post this picture and comment right under the post with the explanation
<br>
<img width="654" alt="APOD Post by Bot" src="https://github.com/Amyat103/Reddit_Space_Bot/assets/109713601/856723a6-a463-4a4f-bbf9-3b2c8ad2ccd3">

<img width="732" alt="Explanation of Image" src="https://github.com/Amyat103/Reddit_Space_Bot/assets/109713601/5d221fde-cfaa-42f2-a67b-edcfdc33a49e">

### This is an example of Daily Random Post, the bot will post 3 random APOD with an explanation in the comment
<br>
<img width="500" alt="Random Gallery Posted by Bot" src="[https://github.com/Amyat103/Reddit_Space_Bot/assets/109713601/9aa3571c-3fa4-4b4b-9b64-be080f6a2e14](https://github.com/Amyat103/Reddit_Space_Bot/assets/109713601/5fa020e3-95bc-4f39-bda6-73e66b48d2be)">

<img width="500" alt="Explanation of Images" src="https://github.com/Amyat103/Reddit_Space_Bot/assets/109713601/9aa3571c-3fa4-4b4b-9b64-be080f6a2e14">

