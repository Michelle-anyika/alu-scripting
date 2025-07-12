#!/usr/bin/python3
"""
This module defines a recursive function `recurse` that queries
the Reddit API and returns a list of all hot article titles
for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieves the titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulator list for hot article titles.
        after (str): Token for the next page of results (for recursion).

    Returns:
        list or None: List of titles or None if subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Agent/1.0"}
    params = {"after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except requests.RequestException:
        return None

