#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('127.0.0.1', 27017)

# Connect to Mongo DB instance for test
db = client['test']

cols = db.collection_names()
for c in cols:
    print('Collection: {0}'.format(c))
    #print(sorted(list(db[c].index_information())))
    #print(sorted(list(db[c].index_information())))
    for i in sorted(list(db[c].index_information())):
        print('    {0}'.format(i))
