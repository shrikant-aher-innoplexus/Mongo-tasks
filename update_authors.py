"""
    (*)2. Extract all Author names from the "authors" array and
    create a new entry in the same record with a different key_name, containing those author names as a comma separated string.
"""


from pymongo import MongoClient
import sys

con = MongoClient('localhost', 27017)
db = con.testData
tab = db.vienna_publications_data_simplified_v1


def update_author_names():
    data = tab.find({}, {'authors.author_name': 1})
    for i in data:
        x = []
        for j in i['authors']:
            x.append(j['author_name'])
        try:
            tab.update({'_id': i['_id']}, {"$set": {'authors_names': x}})
        except:
            print "Exception : ", sys.exc_info()[0]

update_author_names()
