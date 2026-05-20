import redis
import sys
from pathlib import Path
from pymongo import MongoClient

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.transform import transform_function

def load_to_mongodb():

    client = MongoClient("mongodb://192.168.64.1:27017/")
    db = client["my-database"]
    collection = db["animal_shelter"]
    records = transform_function()

    collection.delete_many({})
    collection.insert_many(records)