#!/usr/bin/env python

from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

# Connect to Mongo DB instance for test
db = client['test']

cols = db.collection_names()
for c in cols:
    print(c)

