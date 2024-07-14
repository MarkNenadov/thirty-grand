import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file into a pandas DataFrame and fills NA/NaN values with an empty string.

    Parameters:
        file_path: Full path to CSV file
    """
    return pd.read_csv(file_path, low_memory=False).fillna('')
