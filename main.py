import praw
import secret
import requests
import json
from PIL import Image
import os

#PRAW
def reddit_post(pic):
    #Authenticating via OAuth
    reddit = praw.Reddit(
        client_id=secret.client_id,
        client_secret=secret.client_secret,
        password=secret.password,
        user_agent="my user agent",
        username=secret.username,
    )
    print(reddit.user.me())

    #authorized instance instead of read-only
    print(reddit.read_only)

    #testing subreddit created for this bot
    #obtaining subreddit
    subreddit = reddit.subreddit("SpaceGalleries")
    print(subreddit.display_name)
    print(subreddit.description)

    #obtaining submission instance from a sub
    redditor = reddit.redditor(secret.username)
    print(redditor.link_karma)

    sub_title = "SpaceGalleries"
    title = "APOD TEST"
    image = r"/Users/david/Desktop/space pic.jpeg"

    #Post NASA Image of the day
    reddit.subreddit(sub_title).submit_image(title, image_path=pic)

    #Post NASA Monthly Image recap
    # image1 = "/Users/david/Desktop/space pic.jpeg"
    # image2 = "/Users/david/Desktop/Galaxy_clusters_in_the_cosmic_web.jpg"
    # image3 = "/Users/david/Downloads/345984844_770510188014807_6813628122632339994_n.png"
    # images_gal = [
    #     {"image_path": image1,
    #      "caption": "This is galaxy",
    #      },
    #     {"image_path": image2,
    #      "caption": "This is also galaxy",
    #      },
    #     {"image_path": image3,
    #      "caption": "This is weird tree",
    #      },
    # ]
    # reddit.subreddit(sub_title).submit_gallery(title, images_gal)

#NASA API
#get pic from nasa post on reddit daily

#APOD REQUEST
APOD_params = {
    "date": "",
    "api_key": secret.NASA_API,
}
r = requests.get("https://api.nasa.gov/planetary/apod", params=APOD_params)
print(r.status_code)
print(r)
response = json.loads(r.text)
print(response)
img_link = response["hdurl"]
print(img_link)

#opening image from url to post
image_res = requests.get(img_link)
with open("APOD.jpg", "wb") as image:
    image.write(image_res.content)

#use nasa jpg pink to post on subreddit
reddit_post("APOD.jpg")

os.remove("APOD.jpg")