import pandas as pd

csv_file = 'events.csv'
df = pd.read_csv(csv_file)

# Convert to Parquet
parquet_file = "events.parquet"
df.to_parquet(parquet_file, engine="pyarrow", index=False)

print(f"Converted {csv_file} to {parquet_file}")