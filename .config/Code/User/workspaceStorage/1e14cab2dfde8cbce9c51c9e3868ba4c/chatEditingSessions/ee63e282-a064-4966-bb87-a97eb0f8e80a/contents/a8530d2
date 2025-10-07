import os

data_files = ["semeion.data", "spambase.data"]

semeion_columns = [f"pixel_{i}" for i in range(256)] + [f"label_{i}" for i in range(10)]
df_semeion = pd.read_csv("semeion.data", sep=" ", header=None, names=semeion_columns, engine="python")
df_semeion.to_feather("semeion.feather")

try:
    df_spambase = pd.read_csv("spambase.data", header=None)
except Exception:
    df_spambase = pd.read_csv("spambase.data", header=None, delim_whitespace=True)
df_spambase.to_feather("spambase.feather")