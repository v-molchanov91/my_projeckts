#import psycopg2
#from psycopg2 import Error

#try:
    #connection=psycopg2.connect(user='postgres',
                                #password='1234',
                                #host='localhost',
                                #port='5432',
                                #database='test')
    #cursor=connection.cursor()
    #update_query = """Update mobile set price = 3400 where id = 1;
    #Update mobile set price =7600 where id = 4 """
    #cursor.execute(update_query)
    #connection.commit()
    #count=cursor.rowcount
    #print(count, 'Запись успешно удалена')

    #cursor.execute('Select * from mobile')
    #print('Результат', cursor.fetchall())

#except (Exception, Error) as error:
    #print("Ошибка при работе с PostgreSQL", error)
#finally:
    #if connection:
        #cursor.close()
        #connection.close()
        #print("Соединение с PostgreSQL закрыто")

#import psycopg2
#from psycopg2 import Error

#try:
    #connection=psycopg2.connect(user='postgres',
                                #password='1234',
                                #host='localhost',
                                #port='5432',
                                #database='test')
    #cursor=connection.cursor()
    #delete_query='''Delete from mobile where id = 2 '''
    #cursor.execute(delete_query)
    #connection.commit()
    #count=cursor.rowcount
    #print(count, 'Запись успешно удалена')
    #cursor.execute('Select * from mobile')
    #print('Результат', cursor.fetchall())
#except (Exception, Error) as error:
    #print("Ошибка при работе с PostgreSQL", error)
#finally:
    #if connection:
        #cursor.close()
        #connection.close()
        #print("Соединение с PostgreSQL закрыто")

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432")
    connection.autocommit = True
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = 'create database postgres_db'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")



