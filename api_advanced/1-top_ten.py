#!/usr/bin/python3
"""Query Reddit API for top 10 hot posts in a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'linux:alu-api:v1.0 (by /u/Anonymous)'}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=5
        )
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except (requests.exceptions.RequestException, ValueError):
        print(None)
