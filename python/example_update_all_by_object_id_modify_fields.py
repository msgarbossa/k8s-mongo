#!/usr/bin/env python
# import pymongo
from pymongo import MongoClient
import pprint
import datetime
import os
import sys
from mod_report import *
#import bson
from bson.objectid import ObjectId

client = MongoClient('127.0.0.1', 27017)

db = client['test']

coll_test = db.coll_test

def print_header(header):
    chars = len(header)
    length = chars + 4
    print('#' * length)
    print('# {0} #'.format(header))
    print('#' * length)
    
# This converts date_utc_epoch_ms date_utc_epoch (divides field by 1000 and saves back to collection)
for coll in coll_test.find():
    if coll.has_key('size_kb'):
        id = str(coll['_id'])
        print "id has size_kb: " + id
        file_size_kb = coll['size_kb']
        repo_size_kb = coll['size_kb']
        result = coll.update_one({'_id': ObjectId(id)}, {'$set': { 'file_size_kb': file_size_kb, 'repo_size_kb': repo_size_kb }}, True)
        print('Modified count: {0}'.format(result.modified_count))
        result = coll_test.update_one({'_id': ObjectId(id)}, {'$unset': { 'size_kb': 1 }})
        print('Modified count: {0}'.format(result.modified_count))

