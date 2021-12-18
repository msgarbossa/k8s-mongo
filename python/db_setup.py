#!/usr/bin/env python

import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('127.0.0.1', 27017)

# Connect to Mongo DB instance for test
db = client['test']

# index on a single key
result = db.test_coll.create_index([('name', pymongo.ASCENDING)], unique=True)

# multiple key index
result = db.test_coll.create_index([('date_utc_epoch', pymongo.ASCENDING), ('dob', pymongo.ASCENDING)])

