import datetime
import pymysql
connection = pymysql.connect(host='localhost',
                            password= '',
                            db='Chinook')

try: 
     with connection.cursor() as cursor:
         cursor.execute("""CREATE TABLE IF NOT EXISTS
                            Friends(name char(20), age int, DOB datetime);""")
        
finally:
    connection.close()                                  