"""
    (*)6. Split the string "countries_str" into an array,
    and update the same entry "countries_str" and
    "countries_arr" with the array.
"""

import sys
from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con.testData
tab = db.vienna_publications_data_simplified_v1


def update_countries():
    data = tab.find({}, {'countries_str': 1})
    for i in data:
        try:
            tab.update(
                {'_id': i['_id']},
                {'$set': {'countries_arr': i['countries_str'].split(';')}}
            )
        except:
            print "Exception: ", sys.exc_info()[0]

update_countries()
