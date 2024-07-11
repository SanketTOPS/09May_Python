import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='tops')
    print("Database connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()
#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','baroda'),('hitesh','surat'),('nirav','ahmedabad'),('pratik','rajkot')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set city='gondal' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


#Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)