#!/usr/bin/env python3
""" write something about somekind of nginx log file """
from pymongo import MongoClient



if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    print(nginx_coll.count_documents({}), "logs")
    print("Methods:")
    print("\tmethod GET: {}".format(nginx_coll.count_documents({'method': 'GET'})))
    print("\tmethod POST: {}".format(nginx_coll.count_documents({'method': 'POST'})))
    print("\tmethod PUT: {}".format(nginx_coll.count_documents({'method': 'PUT'})))
    print("\tmethod PATCH: {}".format(nginx_coll.count_documents({'method': 'PATCH'})))
    print("\tmethod DELETE: {}".format(nginx_coll.count_documents({'method': 'DELETE'})))
    print("{} status check".format(nginx_coll.count_documents({'method': 'GET', 'path': '/status'})))
