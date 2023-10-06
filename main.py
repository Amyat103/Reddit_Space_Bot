import praw
import secret

reddit = praw.Reddit(
    client_id=secret.client_id,
    client_secret=secret.client_secret,
    password=secret.password,
    user_agent="my user agent",
    username=secret.username,
)

print(reddit.read_only)