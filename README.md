This project was heavily inspired by @airscholar, you will notice:
1. Similar folder structure.
2. Slight difference in the reddit project.

Find at the end of the page a reference to @airscholar's reddit project, and his YouTube series.

# Reddit ETL Pipeline
In this project we build an ETL pipeline, that ingests its data from a reddit subreddit.

The posts in the subreddit are sorted by `newest`, it can also be sorted by `hot`, `controversial` and `top`. By default it is set to `newest`.

The selftext of all the posts are broken down into word dictionaries, then transformed into a joined dictionary that contains: 
- Each `word` as key.
- The `word count` as the value.

It would be interesting to have a ready tool to analyze patterns in word frequency in different subreddits.

# Folder Structure
Some folders will be ignored as they are currently empty or not in use. Their explanation will be added as additional features are added to the project. Stay tuned!

```
+ ---- config
+ ---- dags
+ ---- data
        + --- input
        + --- output
                word-cloud-dictionary.json
+ ---- etls
        reddit_etl.py
+ ---- logs
+ ---- pipelines
        reddit_pipeline.py
+ ---- plugins
+ ---- tests
+ ---- utils
        constants.py
```

`config`: contains the config file that defines the parameters and the credentials used throughout the project.

⚠️ You will have to fill in the `config.conf` file with your credentials to be able to connect to the Reddit client.

```
[parameters]
top_n = 200
subreddit = Loki

[file_paths]
cloud_output_name = tomc_cloud

[credentials]
reddit_client_secret = [YOUR SECRET]
reddit_client_id = [YOUR ID]
reddit_username = [YOUR REDDIT USERNAME]
reddit_password = [YOUR REDDIT PASSWORD]
```
To get your reddit credentials visit this URL: https://www.reddit.com/wiki/api/.

`data`: currently the `input` data is not saved since the data is directly ingested from reddit: i.e. there is no data caching. `output` contains the output JSON files resulted after running the `reddit_pipeline.py` script.

`utils`: contains a `constants.py` script, which uses the `ConfigParser` library to parse the config file defined earlier.

# How To Run

1. First make sure to set the `config.conf` file as described above. Set the subreddit to any subreddit you would like to ingest from, and the `top_n` parameter to the number of posts you would like to export from.

2. Using the terminal `cd` into `pipelines` and run the `reddit_pipeline.py` script.

```
python3 reddit_pipeline.py
```

# Improvements to be added soon!
1. Add data caching feature.
2. Add feature to toggle between `new`, `hot`, and `controversial` sorted posts.
3. Slight improvements in the cleaning of the selftext corpus ingested from reddit.
4. Dockerize project.
5. Use Apache Airflow web server.
6. Load data on AWS.


# Reference
1. @airscholar reddit project: https://github.com/airscholar/RedditDataEngineering/tree/main.
2. @airscholar youtube channel: https://www.youtube.com/@CodeWithYu