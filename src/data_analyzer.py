import os
import pandas as pd
from collections import Counter


class DataAnalyzer:
    def __init__(self, df):
        self.df = df
        self.add_tweet_words_len_column()
        self.add_tweet_char_len_column()

    def add_tweet_words_len_column(self):
        """ Add a column of each 'Text' (tweet) word length"""
        self.df["Words_len"] = self.df["Text"].apply(lambda x: len(x.split()))

    def add_tweet_char_len_column(self):
        """ Add a column of each 'Text' (tweet) character length"""
        self.df['Tweet_char_len'] = self.df['Text'].apply(lambda x: len(x))


    def count_total_tweets(self):
        return self.df['Text'].value_counts().sum()

    def count_tweets_by_category(self):
        number_of_tweets = self.df['Biased'].value_counts()
        return number_of_tweets.to_dict()


    def get_tweet_length_average(self):
        return self.df['Words_len'].mean()

    def get_tweet_length_average_by_category(self):
        return self.df.groupby('Biased')["Words_len"].mean().to_dict()

    def get_top_3_largest_tweets_by_category(self):
        top_3_tweets_len_df = self.df.drop(columns=['Username', 'Words_len', 'Keyword', 'CreateDate', 'TweetID']).sort_values(['Biased', 'Tweet_char_len']).groupby('Biased').tail(3)
        return top_3_tweets_len_df.to_dict()

    def get_top_3_largest_tweets(self):
        top_3_tweets_len_df = self.df['Tweet_char_len'].sort_values(ascending=False).head(3)
        top_3_tweets = self.df.iloc[top_3_tweets_len_df.index].drop(columns=['Username', 'Words_len', 'Keyword', 'CreateDate', 'TweetID'])
        return top_3_tweets.to_dict()

    def get_10_most_common_words(self):
        ten_most_common_words = Counter(" ".join(self.df["Text"]).split()).most_common(10)
        print(ten_most_common_words)

    @staticmethod
    def count_upper_words_per_row(text):
        words = text.split()
        upper_words = sum([1 for word in words if word.isupper()])
        return upper_words

    def get_shouting_words_by_category(self):
        self.df["upper_words_count"] = self.df['Text'].apply(self.count_upper_words_per_row)
        return self.df.groupby('Biased')["upper_words_count"].sum().to_dict()

    def get_shouting_words(self):
        self.df["upper_words_count"] = self.df['Text'].apply(self.count_upper_words_per_row)
        return self.df["upper_words_count"].sum()
