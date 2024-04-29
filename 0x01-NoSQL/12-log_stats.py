from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    log_count = nginx_coll.count_documents({})
    print(f"{log_count} logs")
    print("Methods:")

    for method in methods:
        method_query = {'method': method}
        count = nginx_coll.count_documents(method_query)
        print(f"\tmethod {method}: {count}")

    status_query = {'method': 'GET', 'path': '/status'}
    status_check = nginx_coll.count_documents(status_query)
    print(f"{status_check} status check")
