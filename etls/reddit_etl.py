"""
    Date of development: 23-04-2024
    PRAW repo @ https://github.com/praw-dev/praw
    PRAW documentation @ https://praw.readthedocs.io/en/stable/
    PRAW: Python Reddit API Wrapper.
"""
import matplotlib.pyplot as plt
import numpy as np
import wordcloud
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

import praw
import sys
import os
import re

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from utils.constants import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_PASSWORD, REDDIT_USERNAME
from nltk.stem.wordnet import WordNetLemmatizer

try:
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        password=REDDIT_PASSWORD,
        user_agent="Creating word cloud",
        username=REDDIT_USERNAME
    )

    print('[i] Reddit client created successfully')
except Exception as e:
    print(e)

    print('[e] Error encountered while creating the Reddit client.')
    sys.exit(1)

def extract_posts_from_subreddit(subreddit_name: str, top_n: int) -> praw.models.listing.generator.ListingGenerator:
    """
        Helper function to extract posts from a subreddit.
    """
    subreddit = reddit.subreddit(subreddit_name)

    new_posts = subreddit.new(limit=top_n)

    return new_posts

def clean_selftext(post: str) -> str:
    """
        Clean text.
    """
    selftext = vars(post)['selftext']
    selftext = selftext.lower()
    selftext = re.sub(r'\n', '', selftext)

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    selftext = selftext.translate(translator)

    # Remove stop words
    selftext = selftext.split()
    useless_words = nltk.corpus.stopwords.words("english")
    useless_words = useless_words + ['hi', 'im']

    selftext_filtered = [word for word in selftext if not word in useless_words]

    # Remove numbers
    selftext_filtered = [re.sub(r'\w*\d\w*', '', w) for w in selftext_filtered]

    # Stem or Lemmatize
    lem = WordNetLemmatizer()
    selftext_lemmatized = [lem.lemmatize(y) for y in selftext_filtered]

    selftext_final = ' '.join(selftext_lemmatized)
    
    return selftext_final

def extract_selftext_from_posts(posts: praw.models.listing.generator.ListingGenerator) -> list:
    """
        Helper function to extract selftext  from posts.
    """
    return [clean_selftext(post) for post in posts]

def transform_selftext_to_wordcloud(selftext: str) -> dict:
    """
        Helper function to transform Reddit selftext to wordcloud.
    """
    wordcloud_instance = wordcloud.WordCloud()

    wc = wordcloud_instance.process_text(selftext)

    return wc

def transform_join_clouds(wordclouds: list) -> dict:
    """
        Join wordclouds together.
    """
    joined_clouds = {}

    for cloud in wordclouds:
        for key in cloud.keys():
            if key not in joined_clouds.keys():
                joined_clouds[key] = 0
            joined_clouds[key] += 1
    
    return joined_clouds
