import pandas as pd
import os

data_files = ["semeion.data", "spambase.data"]

for file in data_files:
    try:
        df = pd.read_csv(file, header=None)
    except Exception:
        df = pd.read_csv(file, header=None, delim_whitespace=True)
    feather_file = file.replace(".data", ".feather")
    df.to_feather(feather_file)