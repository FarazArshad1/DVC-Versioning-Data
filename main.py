import pandas as pd
import os

# create a sample column with column names
data ={
    "Name" : ["Alice", "Bob", "Charlie"],
    "Age" : [25,26,27],
    "City" : ["New York", "Los Anglos", "Chicago"]
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"CSV file Saved to {file_path}")
