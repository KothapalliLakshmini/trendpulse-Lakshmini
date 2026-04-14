import requests as re
import time
import os
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

headers = {"User-Agent": "TrendPulse/1.0"}

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = re.get(url, headers=headers)
data = response.json()[:500]  # First 500

stories = []
for id in data:
    try:
        url1 = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        response_story = re.get(url1, headers=headers)
        story_data = response_story.json()
        stories.append(story_data)
    except Exception as e:
        print(f"Error message:{e}")
        continue
    time.sleep(2)  # Sleep after each fetch

print(f"Collected {len(stories)} stories.")
print(stories)

df = pd.DataFrame(stories)
print(df.columns)
df = df.rename(columns = {"id":"post_id","by":"author","descendants":"num_comments","score":"Number of upvotes"})

df["time"] = pd.to_datetime(df["time"],unit='s')

df["collected_at"]=pd.to_datetime("now")

df["category"] ="technology"

print(df.columns)

categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

categories_list = []

for title in df["title"]:
    title = str(title).lower()
    assigned ="other"
    for category,keywords in categories.items():
        for word in keywords:
            if word.lower() in title:
                assigned = category
                break
        if assigned != "other":
            break
       
      
    categories_list.append(assigned)     

df["category"] = categories_list

print(df["category"])
df= df.sort_values(by="Number of upvotes",ascending = False).groupby("category").head(25)

# Save to CSV
import os
os.makedirs('data', exist_ok=True)

df.to_csv('data/cleaned_trends.csv', index=False)
print("Data saved to data/cleaned_trends.csv")


    
df["collected_at"] = df["collected_at"].astype(str)
df["time"] =df["time"].astype(str)

if not os.path.exists('data'):
    os.makedirs('data')

file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
print(file_name)

with open (file_name, "w+")as f:
   json.dump(df.to_dict(orient='records'), f, indent=4)
   print(f"Total stories collected: {len(df)}")



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