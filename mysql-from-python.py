import pymysql
connection = pymysql.connect(host='localhost',
                            password= '',
                            db='Chinook')

try: 
    with connection.cursor() as cursor:
            rows = cursor.executemany(" Delete from Friends where name = %s;",['Bob', 'Jim'])
            connection.commit()
finally:
    connection.close()                                  