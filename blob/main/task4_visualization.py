import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)


os.makedirs("outputs", exist_ok=True)
top10 = df.sort_values(by="Number of upvotes", ascending=False).head(10)


plt.figure()
plt.barh(top10["title"], top10["Number of upvotes"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")

plt.show()


category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.show()