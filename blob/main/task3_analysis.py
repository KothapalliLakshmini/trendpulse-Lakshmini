import pandas as pd
import numpy as np
import os

# Load CSV
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

print(f"Loaded data: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
avg_score = df["Number of upvotes"].mean()
avg_comments = df["num_comments"].mean()

print(f"Average score   : {avg_score}")
print(f"Average comments: {avg_comments}")
scores = df["Number of upvotes"].values
comments = df["num_comments"].values

print("\n--- NumPy Stats ---")

print(f"Mean score   : {np.mean(scores)}")
print(f"Median score : {np.median(scores)}")
print(f"Std deviation: {np.std(scores)}")
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")


category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()
print(f"\nMost stories in: {top_category} ({top_count} stories)")

max_comments = np.max(comments)
top_story = df[df["num_comments"] == max_comments].iloc[0]

print(f"Most commented story:{top_story['title']} — {top_story['num_comments']} comments")

df["engagement"] = df["num_comments"] / (df["Number of upvotes"] + 1)

df["is_popular"] = df["Number of upvotes"] > avg_score



os.makedirs("data", exist_ok=True)

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")