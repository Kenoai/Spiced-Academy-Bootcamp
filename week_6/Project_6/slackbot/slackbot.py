import requests
import pymongo
from sqlalchemy import create_engine
import psycopg2
import time
import logging

time.sleep(10)  # seconds
# Establish a connection to the MongoDB server

print('connected!')

pg = create_engine('postgresql://em:Emiliepostgres01!@postgresdb:5432/twitter', echo=True)

webhook_url = "https://hooks.slack.com/services/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"

result_set = pg.execute("SELECT * FROM tweets ORDER BY created_at DESC LIMIT 1")  


for r in result_set: 
    r._asdict() 
    data = {
    "text": "new tweet!",
    "blocks": [
        {
            "type": "section","text": {"type": "mrkdwn","text": r['text']},
            "accessory": {"type": "image","image_url": r['image'], "alt_text": "image"}
            },
        {
            "type": "section","text": {"type": "mrkdwn","text": ("Sentiment: " + str(r['sentiment']))}
            }
            ]}

    #print(data)

    requests.post(url=webhook_url, json = data)
    