#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

db = client['test']

coll_test = db.coll_test

result = coll_test.delete_many({})

print('Removed: {0}'.format(result.deleted_count))

