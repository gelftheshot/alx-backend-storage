#!/usr/bin/env python3
"""Script to analyze nginx log file."""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f"{nginx_coll.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        count = nginx_coll.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_coll.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_check} status check")

    pipeline = [
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]

    print("IPs:")
    for doc in nginx_coll.aggregate(pipeline):
        print(f"\t{doc['_id']}: {doc['count']}")
