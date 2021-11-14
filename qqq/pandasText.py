import pandas as pd
import pymysql

host = '127.0.0.1'
port = 3306
user = 'root'
password = '123456'

sql = 'select * from orders'
conn = pymysql.Connect(host=host,user=user,password=password,port=port,database='northwind')
cursor = conn.cursor()
cursor.execute(sql)
out_res = cursor.fetchall()
descr = cursor.description
c = lambda d:[i for i in d]
desc_2_list = c(descr)
descr_list = list(descr)
ex = pd.DataFrame(descr_list)
print(ex.head())



