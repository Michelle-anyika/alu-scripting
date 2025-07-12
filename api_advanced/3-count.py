#!/usr/bin/python3
"""
This module defines a recursive function `count_words` that queries
the Reddit API, parses the titles of hot articles, and counts given
keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=None, after=None, word_count=None):
    """
    Recursively counts occurrences of words in hot article titles.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to search for.
        hot_list (list): List of article titles.
        after (str): Token for pagination.
        word_count (dict): Accumulator for word counts.

    Prints:
        Sorted list of word counts in format: word: count
    """
    if hot_list is None:
        hot_list = []
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'ALU-Student-Agent/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            title = post.get('data', {}).get('title', '').lower()
            hot_list.append(title)

        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after, word_count)

        # Final processing
        # Normalize word list (lowercase, remove duplicates)
        all_words = [word.lower() for word in word_list]
        for word in set(all_words):
            word_count[word] = 0

        # Count each word
        for title in hot_list:
            for word in word_count:
                word_count[word] += title.split().count(word)

        # Filter out zero-counts
        filtered = {k: v for k, v in word_count.items() if v > 0}

        # Sort and print
        for word in sorted(filtered.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(word[0], word[1]))

    except requests.RequestException:
        return

