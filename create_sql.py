

import pandas as pd
import json
import sqlite


with open("C:\\Users\\kleas\\OneDrive\\Έγγραφα\\Ceid\\10 ΕΠΙΛΟΓΗΣ\\Γλωσσική Τεχνολογία\\webcrawler\\articles_body.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.head()   