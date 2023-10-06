import praw
import secret
import requests
import json

#PRAW
def reddit_post():
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
    title = "Test"
    image = r"/Users/david/Desktop/space pic.jpeg"

    #Post NASA Image of the day
    # reddit.subreddit(sub_title).submit_image(title, image)

    #Post NASA Monthly Image recap
    image1 = "/Users/david/Desktop/space pic.jpeg"
    image2 = "/Users/david/Desktop/Galaxy_clusters_in_the_cosmic_web.jpg"
    image3 = "/Users/david/Downloads/345984844_770510188014807_6813628122632339994_n.png"
    images_gal = [
        {"image_path": image1,
         "caption": "This is galaxy",
         },
        {"image_path": image2,
         "caption": "This is also galaxy",
         },
        {"image_path": image3,
         "caption": "This is weird tree",
         },
    ]
    reddit.subreddit(sub_title).submit_gallery(title, images_gal)

#NASA API
#get pic from nasa post on reddit daily

#APOD REQUEST
r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={secret.NASA_API}")
print(r.status_code)


