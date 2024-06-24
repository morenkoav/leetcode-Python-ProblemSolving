'''
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.
'''

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['invalid_length'] = tweets['content'].apply(lambda x: 1 if len(x) > 15 else 0)
    return tweets[tweets.invalid_length == 1][['tweet_id']]
    