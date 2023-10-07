import praw
import secret
import requests
import json
import os
import datetime
from PIL import Image
from io import BytesIO

#PRAW
def reddit_post_daily(pic):
    #Authenticating via OAuth
    reddit = praw.Reddit(
        client_id=secret.client_id,
        client_secret=secret.client_secret,
        password=secret.password,
        user_agent="bot by u/Space_Picture_Bot",
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

    today = datetime.date.today()

    sub_title = "SpaceGalleries"
    title = f"[{today}] NASA Astronomy Picture Of the Day"

    #Post NASA Image of the day
    reddit.subreddit(sub_title).submit_image(title, image_path=pic)


#Post gallery of random
def reddit_post_rand(list):
    reddit = praw.Reddit(
        client_id=secret.client_id,
        client_secret=secret.client_secret,
        password=secret.password,
        user_agent="bot by u/Space_Picture_Bot",
        username=secret.username,
    )
    print(reddit.user.me())

    subreddit = reddit.subreddit("Astronomy_Pics")

    #Post CATALOG
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

def apod_request_single():
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
    #getting the hd link
    img_link = response["hdurl"]
    print(img_link)

    #opening image from url to post
    image_res = requests.get(img_link)
    with open("APOD.jpg", "wb") as image:
        image.write(image_res.content)
    return "APOD.jpg"

#APOD Request 3 random
def apod_ran_req():
    ran_params = {
        "count": 3,
        "api_key": secret.NASA_API,
    }
    r = requests.get("https://api.nasa.gov/planetary/apod", params=ran_params)
    response = json.loads(r.text)
    ran_im_links = []
    for dict in response:
        if "hdurl" in dict:
            url = dict["hdurl"]
        else:
            url = dict["url"]
        date = dict["date"]
        expl = dict["explanation"]
        single_data = {
            "URL": url,
            "Date": date,
            "Explanation": expl,
        }
        ran_im_links.append(single_data)
    return ran_im_links



ran_list_apod = apod_ran_req()



reddit_post_rand(ran_list_apod)






#use nasa response to post on subreddit
#daily single post
# apod_img = apod_request_single()
# reddit_post_daily(apod_img)
#deleting the image after posting
# os.remove("APOD.jpg")

#daily random image from NASA




# # TO GENERATE CODE (AUTH)
# reddit = praw.Reddit(
#         client_id=secret.client_id,
#         client_secret=secret.client_secret,
#         password=secret.password,
#         user_agent="bot by u/Space_Picture_Bot",
#         username=secret.username,
#         redirect_uri="http://localhost:8080",
#     )
#
# print(reddit.auth.url(scopes=["identity"], state=secret.STATE, duration="permanent"))
#


# (MONTHLY CATALOG) MAYBE ADD LATER
# def apod_request_monthly():
#     month_params = {
#         "start_date": "2022-10-12",
#         "end_date": "2022-10-20",
#         "api_key": secret.NASA_API,
#     }
#     r = requests.get("https://api.nasa.gov/planetary/apod", params=month_params)
#     print(r.status_code)
#     response = json.loads(r.text)
#     print(response)

# print(apod_request_monthly())

