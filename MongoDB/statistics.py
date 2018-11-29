# Copyright 2018 Chunshu Wu happycwu@bu.edu

from pymongo import MongoClient
CLIENT = MongoClient('localhost', 27017)

DATABASE = CLIENT.pic_contents
POSTS = DATABASE.posts

def number_of_tags():
    print("\n*********************************************\n")
    for twit_name in POSTS.find().distinct("twit_name"):
        overall_content = set()
        for post in POSTS.find({"twit_name": twit_name}):
            twit_name = post["twit_name"]
            overall_content = overall_content.union(set(post["contents"]))
        count = len(overall_content)
        print("There are "+str(count)+" tags in "+twit_name+"'s tweets")
    print("\n*********************************************\n")

if __name__ == '__main__':
    try:
        number_of_tags()
    except Exception as e:
        print(e)