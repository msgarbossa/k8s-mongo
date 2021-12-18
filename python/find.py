#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['test']

coll_test = db.coll_test

for env in coll_test.find():
    pprint.pprint(env)

