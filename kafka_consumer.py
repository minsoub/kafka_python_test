from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'numtest', 
    bootstrap_servers=['localhost:9092'], 
    auto_offset_reset='earliest', 
    enable_auto_commit=True, 
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

client = MongoClient( #'mongodb://root:root123@localhost:27017/numtest')
      'localhost:27017',  username='root', password='root123')
#db = client['numtest']  #client.numtest.numtest
db = client.numtest

for message in consumer:
    message = message.value
    db.numtest.insert_one(message)
    print('{} added to {}'.format(message, db))


