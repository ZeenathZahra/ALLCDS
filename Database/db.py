import mysql.connector


database=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        port=3348
        )

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE allcds")

print("Database Created..")
