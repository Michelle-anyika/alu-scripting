#!/usr/bin/python3
"""Query the Reddit API and print titles of top 10 hot posts for a subreddit."""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid or an error occurs, prints nothing.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom-Agent/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    if not data:
        return

    posts = data.get("children")
    if not posts:
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
