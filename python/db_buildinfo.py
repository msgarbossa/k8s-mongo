#!/usr/bin/env python

# import pymongo
from pymongo import MongoClient
import pprint
import sys
import os

client = MongoClient('127.0.0.1', 27017)

db = client['test']
pprint.pprint(db.command("buildinfo"))


