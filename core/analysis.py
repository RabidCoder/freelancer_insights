import pandas as pd


def load_data(path='data/freelancer_earnings_bd.csv'):
    df = pd.read_csv(path)
    return df
