import pandas as pd

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
