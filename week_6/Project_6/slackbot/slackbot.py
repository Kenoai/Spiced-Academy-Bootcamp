import requests
import pymongo
#import time
from sqlalchemy import create_engine
import psycopg2
import time


#time.sleep(10)  # seconds
# Establish a connection to the MongoDB server
"""client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter"""

print('connected!')

pg = create_engine('postgresql://em:Emiliepostgres01!@postgresdb:5432/twitter', echo=True)

webhook_url = "https://hooks.slack.com/services/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"

result_set = pg.execute("SELECT text FROM tweets")  

for r in result_set:  
    print(r)
    print(type(r))
    print()
    data = {'text': r}
    print(data)
    print(type(data))
    #requests.post(url=webhook_url, json = data)