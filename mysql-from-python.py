import datetime
import pymysql
connection = pymysql.connect(host='localhost',
                            password= '',
                            db='Chinook')

try: 
    with connection.cursor() as cursor:
            cursor.execute(" Update Friends Set age = 22 where name = 'Bob';")
            connection.commit()
        
finally:
    connection.close()                                  