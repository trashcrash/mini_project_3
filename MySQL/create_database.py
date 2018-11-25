import mysql.connector
from mysql.connector import errorcode
DB_NAME = 'pic_contents'

TABLES = {}
TABLES['twitters'] = (
    "CREATE TABLE `twitters` ("
    "  `twit_no` int(10) NOT NULL,"
    "  `twit_name` varchar(30) NOT NULL UNIQUE,"
    "  PRIMARY KEY (`twit_no`)"
    ") ENGINE=InnoDB")

TABLES['pictures'] = (
    "CREATE TABLE `pictures` ("
    "  `pic_no` int(10) NOT NULL,"
    "  `twit_no` int(10) NOT NULL,"
    "  `pic_url` varchar(150) NOT NULL UNIQUE,"
    "  FOREIGN KEY (`twit_no`) REFERENCES `twitters` (`twit_no`) ON DELETE CASCADE, "
    "  PRIMARY KEY (`pic_no`)"
    ") ENGINE=InnoDB")

TABLES['contents'] = (
    "CREATE TABLE `contents` ("
    "  `content_no` int(10) NOT NULL,"
    "  `content_name` varchar(30) NOT NULL UNIQUE,"
    "  PRIMARY KEY (`content_no`)"
    ") ENGINE=InnoDB")

TABLES['pic_content'] = (
    "CREATE TABLE `pic_content` ("
    "  `pic_no` int(10) NOT NULL, "
    "  `content_no` int(10) NOT NULL, "
    "  PRIMARY KEY (`pic_no`,`content_no`), KEY `pic_no` (`pic_no`),"
    "  KEY `content_no` (`content_no`),"
    "  FOREIGN KEY (`pic_no`) REFERENCES `pictures` (`pic_no`) ON DELETE CASCADE, "
    "  FOREIGN KEY (`content_no`) REFERENCES `contents` (`content_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

USERNAME = input("Please enter your MySQL username: \n")
PASSWORD = input("Please enter your password: \n")
cnx = mysql.connector.connect(user = USERNAME, password = PASSWORD)
cursor = cnx.cursor()
cursor.execute("DROP DATABASE "+DB_NAME)
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exist.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
