#!/usr/bin/env python3
"""function that returns all students sorted by average score """
import pymongo


def top_students(mongo_collection):
    for doc in mongo_collection.find():
        total = 0
        leng = len(doc['topics'])
        for sub in doc['topics']:
            total += sub['score']
        avr = total / leng
    mongo_collection.update_many(
        {'_id': doc['_id']},
        {'$set': {'averageScore': avr}}
    )
    return mongo_collection.find().sort('averageScore', pymongo.DESCENDING)
