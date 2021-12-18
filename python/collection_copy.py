#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient
import pprint
import sys
import os

if not len(sys.argv) == 3:
    print("2 arguments must be supplied")
    print(os.path.basename(__file__) + " <source_collection> <destination_collection>")
    sys.exit(1)

source_name = sys.argv[1]
destination_name = sys.argv[2]

client = MongoClient('127.0.0.1', 27017)

db = client['test']

source_collection = db[source_name]

pipeline = [ {"$match": {}}, 
             {"$out": destination_name},
]
source_collection.aggregate(pipeline)

