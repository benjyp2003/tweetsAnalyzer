import os
import pandas as pd


class DataLoader:

    @staticmethod
    def load_df(path):
        try:
            if DataLoader.validate_path(path):
                df = pd.read_csv(path)
                return df
            else:
                print("Path doesn't exist")
                return None
        except Exception as e:
            print(f"Failed to load df from {path}: {e}")

    @staticmethod
    def validate_path(path):
        if not os.path.exists(path):
            return False
        else:
            return True
