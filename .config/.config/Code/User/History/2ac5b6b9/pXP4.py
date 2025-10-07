import pandas as pd
import timeit
from memory_profiler import memory_usage
import os

# Step 1: Read CSV and save in multiple formats
csv_path = "test.csv"
df = pd.read_csv(csv_path)

# Save as JSON, Parquet, and Feather
df.to_json("test.json", orient="records", lines=True)
df.to_parquet("test.parquet", engine="pyarrow")
df.to_feather("test.feather")

print("Files saved in JSON, Parquet, and Feather formats.")

# Step 2 & 3: Load 100MB data and profile load time and memory

def load_json():
    pd.read_json("test.json", orient="records", lines=True)

def load_parquet():
    pd.read_parquet("test.parquet")

def load_feather():
    pd.read_feather("test.feather")

# You can trim the file to approx. 100MB if it's bigger (optional)
# We assume all formats are close in size

def profile(func, name):
    print(f"\nProfiling {name} load:")
    mem_usage = memory_usage((func,), interval=0.1, timeout=10)
    time_taken = timeit.timeit(func, number=1)
    print(f"{name} Load Time: {time_taken:.4f} sec")
    print(f"{name} Peak Memory: {max(mem_usage) - min(mem_usage):.4f} MiB")

profile(load_json, "JSON")
profile(load_parquet, "Parquet")
profile(load_feather, "Feather")

# Step 4: Identify efficient stream for continuous variables
# Let's say continuous variables are all float columns
float_cols = df.select_dtypes(include=['float64', 'float32']).columns
print(f"\nContinuous variables: {list(float_cols)}")

# Estimate file size for continuous variables only
df_cont = df[float_cols]
df_cont.to_json("cont.json", orient="records", lines=True)
df_cont.to_parquet("cont.parquet", engine="pyarrow")
df_cont.to_feather("cont.feather")

print("\nFile sizes for continuous variables:")
print(f"JSON: {os.path.getsize('cont.json') / 1024 / 1024:.2f} MB")
print(f"Parquet: {os.path.getsize('cont.parquet') / 1024 / 1024:.2f} MB")
print(f"Feather: {os.path.getsize('cont.feather') / 1024 / 1024:.2f} MB")
