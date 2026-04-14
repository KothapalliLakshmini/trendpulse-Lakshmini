import os
import json
from datetime import datetime
    
df["collected_at"] = df["collected_at"].astype(str)
df["time"] =df["time"].astype(str)

if not os.path.exists('data'):
    os.makedirs('data')

file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
print(file_name)

with open (file_name, "w+")as f:
   json.dump(df.to_dict(orient='records'), f, indent=4)
   print(f"Total stories collected: {len(df)}")