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
    id = str(coll['_id'])
    date_utc_epoch_ms = int(coll['date_utc_epoch'])
    if date_utc_epoch_ms > 1506443789000:
        date_utc_epoch = date_utc_epoch_ms / 1000
        print(id)
        print(date_utc_epoch_ms)
        print(date_utc_epoch)
        result = coll_test.update_one({'_id': ObjectId(id)}, {'$set': { 'date_utc_epoch': date_utc_epoch }}, True)
        #print('Modified count: {0}'.format(result.modified_count))
        pprint.pprint(coll)
        print('\n')

