#!/usr/bin/env python3
""" list all doc in the collection """


def list_all(mongo_collection):
    """ list all cod in collection """
    return mongo_collection.find()
