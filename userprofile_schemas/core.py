"""Main module."""

import os
import pandas as pd


def extract_schema_from_csvs(path):
    """Extracts the SQL schema of a single CSV file or from a folder containing CSV files."""
    print(path)
    if os.path.isdir(path):
        schema = ""
        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                schema += _extract_schema_from_csv(os.path.join(path, filename)) + "\n"
        return schema
    else:
        return _extract_schema_from_csv(path)
    

def _extract_schema_from_csv(filepath):
    """Extracts the SQL schema from a single CSV file."""
    df = pd.read_csv(filepath, engine='python')
    return pd.io.sql.get_schema(df, os.path.basename(filepath))