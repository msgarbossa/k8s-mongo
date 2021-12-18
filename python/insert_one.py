#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

db = client['test']

coll_test = db.coll_test

data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun',
    'author': 'Bob'
}
result = coll_test.insert_one(data)

print('One post: {0}'.format(result.inserted_id))

