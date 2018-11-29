# Copyright 2018 Chunshu Wu happycwu@bu.edu

from pymongo import MongoClient

CLIENT = MongoClient('localhost', 27017)

DATABASE = CLIENT.pic_contents
POSTS = DATABASE.posts

def find_twitter_name(content):
    print("\n*********************************************\n")
    for post in POSTS.find({"contents": content}):
        twit_name = post.get('twit_name', [])
        print(content+" is in "+twit_name+"'s tweets")
        break
    print("\n*********************************************\n")

if __name__ == '__main__':
    try:
        content = input("Please enter the content you wish to search: ")
        find_twitter_name(content)
    except Exception as e:
        print(e)