import pandas as pd
import timeit
from memory_profiler import memory_usage

test_data = pd.read_csv('test_data.csv')

test_data.to_json('test_data.json', orient='records', lines=True)
test_data.to_parquet('test_data.parquet', index=False)
test_data.to_feather('test_data.feather')
print("Data conversion completed successfully.")

def load_json():
    return pd.read_json(test_data.json, lines=True)

def load_parquet():
    return pd.read_parquet(test_data.parquet)

def load_feather():
    return pd.read_feather(test_data.feather)

print("Timing (in seconds):")
print("JSON:", timeit.timeit(load_json, number=5))
print("Parquet:", timeit.timeit(load_parquet, number=5))
print("Feather:", timeit.timeit(load_feather, number=5))