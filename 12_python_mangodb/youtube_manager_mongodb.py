from pymongo import MongoClient

client = MongoClient("mongodb+srv://Youtubepy:Youtubepy@cluster0.lcumh.mongodb.net/")
 #not a good idea to  include  id and password in code files

db = client["yutube"]
video_collection = db["videos"]

print(video_collection)
