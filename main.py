import praw
import secret

reddit = praw.Reddit(
    client_id=secret.client_id,
    client_secret=secret.client_secret,
    password=secret.password,
    user_agent="my user agent",
    username=secret.username,
)

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

