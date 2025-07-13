#!/usr/bin/python3
"""Query Reddit API and print titles of top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom-Agent"}
    params = {"limit": 10}

    try:
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if res.status_code != 200:
            return

        data = res.json().get("data")
        posts = data.get("children")

        for post in posts:
            print(post.get("data").get("title"))

    except Exception:
        return
