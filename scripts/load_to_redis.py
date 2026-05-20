import redis
from pymongo import MongoClient


def load_to_redis():
    r = redis.Redis(host= '192.168.64.1', port=6379, db=1, decode_responses=True)
    client = MongoClient("mongodb://192.168.64.1:27017/")
    db = client["my-database"]
    collection = db["animal_shelter"]

    avg_stay = list(collection.aggregate([{"$group" : {"_id": None, "avg_shelter_days": {"$avg": "$days_in_shelter"}}}]))[0]["avg_shelter_days"]
    adopted = collection.count_documents({"outcome": "adopted"})

    r.set("avg_stay", avg_stay)
    r.set("total_adoptions", adopted)