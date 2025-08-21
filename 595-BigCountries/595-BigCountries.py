# Last updated: 8/21/2025, 12:25:24 PM
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]
    return invalid_tweets_df[['tweet_id']]
    