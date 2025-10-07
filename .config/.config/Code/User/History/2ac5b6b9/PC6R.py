import pandas as pd
import timeit
from memory_profiler import memory_usage

# Step 1: Download a ~100MB dataset
url = "test.csv"
df = pd.read_csv(url)

# Save dataset in different formats
df.to_json("people.json", orient="records", lines=True)
df.to_parquet("people.parquet")
df.to_feather("people.feather")

# Step 2 & 3: Load each format and measure performance
def profile_load(file_type):
    if file_type == "json":
        stmt = "pd.read_json('people.json', lines=True)"
    elif file_type == "parquet":
        stmt = "pd.read_parquet('people.parquet')"
    elif file_type == "feather":
        stmt = "pd.read_feather('people.feather')"
    else:
        raise ValueError("Unsupported file type")

    # Time the execution over 3 runs
    exec_time = timeit.timeit(stmt, globals=globals(), number=3)

    # Memory profiling: peak memory usage
    mem_usage = max(memory_usage((eval, (stmt,), {"globals": globals()})))

    return exec_time, mem_usage

# Step 4: Run profiling for each format
formats = ["json", "parquet", "feather"]
results = []

for fmt in formats:
    t, m = profile_load(fmt)
    results.append({
        "Format": fmt,
        "Time (s)": round(t, 3),
        "Memory (MB)": round(m, 3)
    })

# Display results
result_df = pd.DataFrame(results)
print(result_df)

# Identify most efficient format for continuous variables
best = result_df.sort_values(by=["Time (s)", "Memory (MB)"]).iloc[0]
print(f"Most efficient format: {best['Format']}")
