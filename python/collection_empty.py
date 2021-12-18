#!/usr/bin/env python

from pymongo import MongoClient
import os
import sys

if not len(sys.argv) == 2:
    print("1 argument must be supplied")
    print(os.path.basename(__file__) + " <collection>")
    sys.exit(1)

collection_name = sys.argv[1]

client = MongoClient('127.0.0.1', 27017)

db = client['test']

coll = db[collection_name]

result = coll.delete_many({})

print('Removed: {0}'.format(result.deleted_count))

