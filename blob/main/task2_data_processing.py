import pandas as pd
import os

# Load JSON
file_path = "data/trends_20260414.json"  

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")


df = df.drop_duplicates(subset=["post_id"])
print(f"After removing duplicates: {len(df)}")


df = df.dropna(subset=["post_id", "title", "Number of upvotes"])
print(f"After removing nulls: {len(df)}")


df["Number of upvotes"] = df["Number of upvotes"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)


df = df[df["Number of upvotes"] >= 5]
print(f"After removing low scores: {len(df)}")


df["title"] = df["title"].str.strip()


os.makedirs("data", exist_ok=True)

output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")


print("\nStories per category:")
print(df["category"].value_counts())
