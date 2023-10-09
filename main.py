import praw
import requests
import json
import os
import datetime
import schedule
import time

#PRAW
os.environ["TZ"] = "America/New_York"
time.tzset()

#PRAW
def reddit_post_daily():
    apod_img, explanation, title = apod_request_single()
    #Obtaining Reddit Instance
    reddit = praw.Reddit(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        password=os.environ.get('PASSWORD'),
        user_agent="bot by u/Space_Picture_Bot",
        username=os.environ.get('USERNAME'),
    )
    print(reddit.user.me())

    #authorized instance instead of read-only
    print(reddit.read_only)

    today = datetime.date.today()

    sub_title = "Astronomy_Pics"
    title = f"[{today}] NASA Astronomy Picture Of the Day. Title: {title}"

    #Post NASA Image of the day
    submission = reddit.subreddit(sub_title).submit_image(title, image_path=apod_img)
    submission.reply(f"{explanation}")




#Post gallery of random
def reddit_post_rand():
    ran_list_apod = apod_ran_req()
    #Obtaining Reddit Instance
    reddit = praw.Reddit(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        password=os.environ.get('PASSWORD'),
        user_agent="bot by u/Space_Picture_Bot",
        username=os.environ.get('USERNAME'),
    )
    print(reddit.user.me())

    title = f"Daily 3 Random APOD, Pic 1 Title:{ran_list_apod[0]['title']}, Pic 2 Title:{ran_list_apod[1]['title']}, Pic 3 Title:{ran_list_apod[2]['title']}"
    subreddit = "Astronomy_Pics"

    #Post CATALOG
    image1 = "APOD0.jpg"
    image2 = "APOD1.jpg"
    image3 = "APOD2.jpg"
    images_gal = [
        {"image_path": image1,
         "caption": ran_list_apod[0]["Explanation"][:180],
         },
        {"image_path": image2,
         "caption": ran_list_apod[1]["Explanation"][:180],
         },
        {"image_path": image3,
         "caption": ran_list_apod[2]["Explanation"][:180],
         },
    ]
    reddit.subreddit(subreddit).submit_gallery(title, images_gal)


#get pic from nasa post on reddit daily
def apod_request_single():
    #APOD REQUEST
    APOD_params = {
        "date": "",
        "api_key": os.environ.get('NASA_API'),
    }
    r = requests.get("https://api.nasa.gov/planetary/apod", params=APOD_params)
    print(r.status_code)
    print(r)
    response = json.loads(r.text)
    print(response)
    #getting the hd link
    img_link = response["hdurl"]
    print(img_link)

    explanation = response["explanation"]
    title = response["title"]

    #opening image from url to post
    image_res = requests.get(img_link)
    with open("APOD.jpg", "wb") as image:
        image.write(image_res.content)
    return "APOD.jpg", explanation, title


#APOD Request 3 random
def apod_ran_req():
    ran_params = {
        "count": 3,
        "api_key": os.environ.get('NASA_API'),
    }
    r = requests.get("https://api.nasa.gov/planetary/apod", params=ran_params)
    response = json.loads(r.text)
    ran_im_links = []
    e = 0
    for dict in response:
        if "hdurl" in dict:
            url = dict["hdurl"]
        else:
            url = dict["url"]
        date = dict["date"]
        expl = dict["explanation"]
        title = dict["title"]
        single_data = {
            "URL": url,
            "Date": date,
            "Explanation": expl,
            "Title": title,
        }

        ran_im_links.append(single_data)

        image_res = requests.get(url)

        image_name = f"APOD{e}.jpg"
        with open(image_name, "wb") as image:
            image.write(image_res.content)
        e += 1
    return ran_im_links


def remove_gal():
    for int in range(3):
        os.remove(f"APOD{int}.jpg")


def remove_pic():
    os.remove("APOD.jpg")


def main():
    print("Script has started.")
    # daily single post
    schedule.every().day.at("00:00").do(reddit_post_daily)

    # deleting the image after posting
    schedule.every().day.at("00:01").do(remove_pic)

    # daily gallery post
    schedule.every().day.at("00:01").do(reddit_post_rand)

    # deleting the image after posting
    schedule.every().day.at("00:05").do(remove_gal)

    while True:
        schedule.run_pending()
        time.sleep(40)

print("checking")
if __name__ == "__main__":
    main()







#daily random image from NASA
#-------------------------------------

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
#---------------------------------------

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

