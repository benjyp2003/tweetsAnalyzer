import json

from src.data_analyzer import DataAnalyzer
from src.data_loader import DataLoader


class Manager:
    def __init__(self, path = r"C:\Users\benjy\PycharmProjects\tweetsAnalyzer\data\tweets_dataset.csv"):
        self.path = path


    def save_analyzed_data(self):

        data_loader = DataLoader()
        df = data_loader.load_df(self.path)

        data_analyzer = DataAnalyzer(df)

        # build the analyzed data for saving to a json
        analyzed_dict = {
            "total_tweets":
                {
                    "antisemitic": int(data_analyzer.count_tweets_by_category()[1]),
                    "non_antisemitic": int(data_analyzer.count_tweets_by_category()[0]),
                    "total": int(data_analyzer.count_total_tweets()),
                    "unspecified": 0
                },
            "average_length":
                {
                    "antisemitic": data_analyzer.get_tweet_length_average_by_category()[1],
                    "non_antisemitic": data_analyzer.get_tweet_length_average_by_category()[0],
                    "total": data_analyzer.get_tweet_length_average()
                },
            "common_words":
                {
                    "total":
                        data_analyzer.get_10_most_common_words()
                },
            "longest_3_tweets":
                {
                    "total": [
                        data_analyzer.get_top_3_largest_tweets()
                    ],
                    "antisemitic / non_antisemitic": [
                        data_analyzer.get_top_3_largest_tweets_by_category()
                    ]
                },
            "uppercase_words":
                {
                    "antisemitic": data_analyzer.get_shouting_words_by_category()[0],
                    "non_antisemitic": data_analyzer.get_shouting_words_by_category()[1],
                    "total": data_analyzer.get_shouting_words()
                }
        }

        # save the dict to a json file
        with open("results/result.json", "w") as json_file:
            json.dump(analyzed_dict, json_file, indent=4, default=str)


