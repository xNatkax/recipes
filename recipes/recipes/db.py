from pymongo import MongoClient

client = MongoClient("mongodb://admin:pass@localhost:27017/")

recipes_collection = client.db.recipes

if __name__ == "__main__":
    from rich import print

    print(recipes_collection.find_one())
