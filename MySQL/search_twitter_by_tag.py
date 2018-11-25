import mysql.connector
from mysql.connector import errorcode
USERNAME = input("Please enter your MySQL username: \n")
PASSWORD = input("Please enter your password: \n")
tag_name = input("Please enter the tag you would like to search: \n")
print('\n****************************************\n')
cnx = mysql.connector.connect(user = USERNAME, password = PASSWORD, database = 'pic_contents')
cursor = cnx.cursor()
cursor.execute("SELECT content_no FROM contents WHERE content_name = '"+tag_name+"'")
content_no = cursor.fetchall()[0][0]
cursor.execute("SELECT pic_no FROM pic_content WHERE content_no = '"+str(content_no)+"'")
pic_nos = cursor.fetchall()
twitter_nos = set()
for pic_no in pic_nos:
    cursor.execute("SELECT twit_no FROM pictures WHERE pic_no = '"+str(pic_no[0])+"'")
    twitter_no = cursor.fetchall()
    twitter_nos.add(twitter_no[0][0])
for twitter_no in twitter_nos:
    cursor.execute("SELECT twit_name FROM twitters WHERE twit_no = '"+str(twitter_no)+"'")
    print(cursor.fetchall()[0][0])
cursor.close()
cnx.close()
print('\n****************************************\n')