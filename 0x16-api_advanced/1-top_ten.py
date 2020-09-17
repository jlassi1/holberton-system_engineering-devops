#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ function top_ten"""
    header = {'User-agent': 'Holberton_school'}
    req = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers=header, allow_redirects=False).json()
    try:
        for i in range(10):
            path = req.get('data').get('children')
            print(path[i].get('data').get('title'))
        return
    except Exception:
        pass
    print(None)
    return
