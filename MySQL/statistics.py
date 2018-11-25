import mysql.connector
from mysql.connector import errorcode
USERNAME = input("Please enter your MySQL username: \n")
PASSWORD = input("Please enter your password: \n")
print('\n****************************************\n')
cnx = mysql.connector.connect(user = USERNAME, password = PASSWORD, database = 'pic_contents')
cursor = cnx.cursor()
cursor.execute("SELECT content_no FROM contents")
content_nos = cursor.fetchall()
content_count = 0
for content_no in content_nos:
    cursor.execute("SELECT COUNT(*) FROM pic_content WHERE content_no = '"+str(content_no[0])+"'")
    count = cursor.fetchall()[0][0]
    if count >= content_count:
        content_count = count

for content_no in content_nos:
    cursor.execute("SELECT COUNT(*) FROM pic_content WHERE content_no = '"+str(content_no[0])+"'")
    count = cursor.fetchall()[0][0]
    if count >= content_count:
        cursor.execute("SELECT content_name FROM contents WHERE content_no = '"+str(content_no[0])+"'")
        content_name = cursor.fetchall()[0][0]
        print("The most popular tag is {}, which appears {} times".format(content_name, count))

cursor.execute("SELECT twit_no FROM twitters")
twit_nos = cursor.fetchall()
for twit_no in twit_nos:
    cursor.execute("SELECT twit_name FROM twitters WHERE twit_no = '"+str(twit_no[0])+"'")
    twit_name = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(*) FROM pictures WHERE twit_no = '"+str(twit_no[0])+"'")
    count = cursor.fetchall()[0][0]
    print("There are {} pictures collected from {} in your database. ".format(count, twit_name))
cursor.close()
cnx.close()
print('\n****************************************\n')