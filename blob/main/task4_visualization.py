import matplotlib.pyplot as plt

df.groupby("category")["Number of upvotes"].mean().plot(kind='bar')

plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")

plt.show()

plt.hist(df["Number of upvotes"])

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()