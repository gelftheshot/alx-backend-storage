#!/usr/bin/env python3
""" Python function that changes all topics
    of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ update the mongodb name and topic """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
