import pandas as pd
import os

# List of .data files to convert
data_files = ["semeion.data", "spambase.data"]

for file in data_files:
    # Read the .data file (assuming comma or whitespace separated)
    # Try comma first, fallback to whitespace
    try:
        df = pd.read_csv(file, header=None)
    except Exception:
        df = pd.read_csv(file, header=None, delim_whitespace=True)
    # Save as .feather
    feather_file = file.replace(".data", ".feather")
    df.to_feather(feather_file)