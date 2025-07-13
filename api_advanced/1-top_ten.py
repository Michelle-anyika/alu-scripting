#!/usr/bin/python3
"""
This module prints the titles of the first 10 hot posts
for a given subreddit using Reddit's public API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If subreddit is invalid, prints 'None'.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'Custom-User-Agent'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
