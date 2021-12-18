#!/usr/bin/env python

from pymongo import MongoClient
import pprint
import sys
import os

if not len(sys.argv) == 2:
    print("1 argument must be supplied")
    print(os.path.basename(__file__) + " <collection>")
    sys.exit(1)

collection_name = sys.argv[1]

client = MongoClient('127.0.0.1', 27017)

db = client['test']
collection = db[collection_name]

# Remove all documents, or make modifications. 
collection.remove({}) 
