import pandas as pd
import timeit
from memory_profiler import memory_usage

# Step 1: Download dataset and convert to JSON, Parquet, Feather
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"  # Example dataset
df = pd.read_csv(url)

# To simulate ~100MB, repeat the data
repeat_factor = int(100 * 1024 * 1024 / df.memory_usage(deep=True).sum())
df_large = pd.concat([df] * repeat_factor, ignore_index=True)

df_large.to_json("data.json")
df_large.to_parquet("data.parquet")
df_large.to_feather("data.feather")

# Step 2 & 3: Load 100MB dataset in each format and profile
def load_json():
    pd.read_json("data.json")

def load_parquet():
    pd.read_parquet("data.parquet")

def load_feather():
    pd.read_feather("data.feather")

for fmt, func in [("JSON", load_json), ("Parquet", load_parquet), ("Feather", load_feather)]:
    t = timeit.timeit(func, number=1)
    mem = max(memory_usage((func,)))
    print(f"{fmt}: Time={t:.2f}s, Peak Memory={mem:.2f}MB")

# Step 4: Identify efficient stream for continuous variables
# For continuous variables, Parquet and Feather are columnar and efficient.
print("Parquet and Feather formats are generally more efficient for continuous variables due to their columnar storage.")

