import configparser
import sys
import os

project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, project_directory)

config_directory = os.path.join(project_directory, 'config/config.conf')

parser = configparser.ConfigParser()
parser.read(config_directory)

REDDIT_CLIENT_SECRET = parser.get(section='credentials', option='reddit_client_secret')
REDDIT_CLIENT_ID = parser.get(section='credentials', option='reddit_client_id')
REDDIT_USERNAME = parser.get(section='credentials', option='reddit_username')
REDDIT_PASSWORD = parser.get(section='credentials', option='reddit_password')

CLOUD_OUTPUT_NAME = parser.get(section='file_paths', option='cloud_output_name')

REDDIT_SUBREDDIT = parser.get(section='parameters', option='subreddit')
REDDIT_TOP_N = parser.get(section='parameters', option='top_n')