import requests as re
import time

headers = {"User-Agent": "TrendPulse/1.0"}

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = re.get(url, headers=headers)
data = response.json()[:10]  # Limit to 10 for quick run

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