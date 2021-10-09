

import pandas as pd
import json
import sqlite3


# Open JSON data
with open("C:..\\article_body.json") as f:
    data = json.load(f)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)
df.insert(0, 'Id', range(0, 0 + len(df)))

print(df)


conn=sqlite3.connect("article.db")
c=conn.cursor()


df.to_sql("article",conn)





