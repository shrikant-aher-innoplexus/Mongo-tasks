"""
    (*)8. Using pymongo extract the first half of the data and \
    insert into a new collection, with a name of your choice,
    and the second half into another collection.
"""

from pymongo import MongoClient
import sys

con = MongoClient('localhost', 27017)
db = con.testData
tab = db.vienna_publications_data_simplified_v1


def split_coll():
    count = 0
    half_count = tab.count() / 2
    for data in tab.find():
        if count < half_count:
            try:
                db.collection1.insert(data)
            except:
                print "Exception :", sys.exc_info()[0]
            count += 1
        else:
            try:
                db.collection2.insert(data)
            except:
                print "Exception :", sys.exc_info()[0]

split_coll()
