import mysql.connector
import pymysql
from sqlalchemy import create_engine
import pandas as pd

try:
    conn=mysql.connector.connect(host='database-1.cnqnfmdhai0m.ap-northeast-1.rds.amazonaws.com',user='admin',password='fcbarcelona')
    mycursor=conn.cursor()
    print('Connection established')

except:
    print('Connection error')


# mycursor.execute('CREATE DATABASE IF NOT EXISTS indigo')
# conn.commit()

# mycursor.execute(
#     '''
#     create table airport(
#     airport_id int primary key,
#     code varchar (10) not null,
#     city varchar (50) not null,
#     name varchar (255) not null
#     )
#     '''
# )
#
# conn.commit()


# mycursor.execute('''
# # insert into airport(airport_id,code,city,name)
# # Values(1,'Del','New Delhi','IGIA'),
# #       (2,'CCU','Kolkata','NSCA'),
# #       (3,'BOM','Mumbai','CSMA');
# # ''')
# #
# # conn.commit()


# mycursor.execute('select * from airport where airport_id>1;')
# data=mycursor.fetchall()
# print(data)


# mycursor.execute("update airport set name='Bombay' where airport_id=3")
# conn.commit()

# mycursor.execute('Delete from airport where airport_id = 3')
# conn.commit()

# mycursor.execute('CREATE DATABASE indigo')
# conn.commit()

df=pd.read_csv('flights_cleaned - flights_cleaned.csv')
df2=pd.read_csv('flights_cleaned - flights_cleaned.csv')

engine = create_engine("mysql+pymysql://admin:fcbarcelona@database-1.cnqnfmdhai0m.ap-northeast-1.rds.amazonaws.com/indigo")
df2.to_sql('flights2',con=engine)
