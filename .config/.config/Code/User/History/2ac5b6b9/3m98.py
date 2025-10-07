import pandas as pd
import timeit
from memory_profiler import memory_usage

url = "test.csv" 
df = pd.read_csv(url)

repeat_factor = int(100 * 1024 * 1024 / df.memory_usage(deep=True).sum())
df_large = pd.concat([df] * repeat_factor, ignore_index=True)

df_large.to_json("data.json")
df_large.to_parquet("data.parquet")
df_large.to_feather("data.feather")


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


print("Parquet and Feather formats are generally more efficient for continuous variables due to their columnar storage.")

