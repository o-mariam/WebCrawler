import nltk 
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import joblib
import sqlite3
from nltk.util import Trie
import pandas as pd



import json


stop_words=stopwords.words("english")
stop_words.extend(["said", "i", "it", "you", "and","that","the","(",")",".",","])
print(stop_words)


conn = sqlite3.connect('./article.db')
conn.row_factory = sqlite3.Row       

cursor = conn.execute("SELECT article_body FROM article")




filtered_sent=[]


for row in cursor:
    article_body= row['article_body']           
    tokenized_word=word_tokenize(article_body)
    
  
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
       
  

    

#print("Tokenized Sentence:",word_tokenize)

#print("Filterd Sentence:",filtered_sent)










  

  



        
       
    








    

