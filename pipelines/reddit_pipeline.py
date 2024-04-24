import json
import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from etls.reddit_etl import extract_posts_from_subreddit, extract_selftext_from_posts,\
                            transform_selftext_to_wordcloud, transform_join_clouds

from utils.constants import CLOUD_OUTPUT_NAME, REDDIT_SUBREDDIT, REDDIT_TOP_N

def reddit_pipeline() -> dict:
    """
        Setup Reddit cloudword pipeline.
    """
    subreddit_generator = extract_posts_from_subreddit(subreddit_name=REDDIT_SUBREDDIT, top_n=int(REDDIT_TOP_N))

    selftexts = extract_selftext_from_posts(posts=subreddit_generator)

    wordclouds = []

    for selftext in selftexts:
        wordcloud = transform_selftext_to_wordcloud(selftext)
        
        wordclouds.append(wordcloud)
    
    joined_cloud = transform_join_clouds(wordclouds)

    # Sort it by value
    joined_cloud = dict(sorted(joined_cloud.items(), key=lambda item: item[1], reverse=True))

    print('[i] Final wordcloud set.')
    
    return joined_cloud

if __name__ == '__main__':
    wordcloud = reddit_pipeline()

    output_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(output_dir, 'data/output', CLOUD_OUTPUT_NAME)

    output_dir = f'{output_dir}.json'

    with open(output_dir, 'w') as json_file:
        print('[i] Cloud JSON file saved.')
        json.dump(wordcloud, json_file)