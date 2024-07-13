import pandas as pd


def read_csv(file_path):
    result = pd.read_csv(file_path, low_memory=False)
    result.fillna('')

    return result
