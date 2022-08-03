import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

time.sleep(10)  # seconds
# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter

docs = db.tweets.find()

pg = create_engine('postgresql://em:Emiliepostgres01!@postgresdb:5432/twitter', echo=True)

pg.execute('''CREATE TABLE IF NOT EXISTS tweets 
    (text VARCHAR(500),
    sentiment NUMERIC);''')

for doc in docs:
    #print(doc)
    text = doc['text']
    sentiment = s.polarity_scores(text)  # assuming your JSON docs have a text field
    #print(sentiment)
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))




