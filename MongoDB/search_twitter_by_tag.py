# Copyright 2018 Chunshu Wu happycwu@bu.edu

from pymongo import MongoClient
import pprint

CLIENT = MongoClient('localhost', 27017)

DATABASE = CLIENT.pic_contents
POSTS = DATABASE.posts

def find_tags_in_Twitter_ID(content):
    for post in POSTS.find({"contents": content}):
        twit_name = post.get('twit_name', [])
        print("\n*********************************************\n")
        print(content+" is in "+twit_name+"'s tweets")
        break

if __name__ == '__main__':
    try:
        content = input("Please enter the content you wish to search: ")
        find_tags_in_Twitter_ID(content)
    except Exception as e:
        print(e)