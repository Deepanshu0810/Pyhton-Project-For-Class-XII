import mysql.connector as sqltor
mydb=sqltor.connect(host='localhost',user='root',password='123456',charset='utf8')
if mydb.is_connected():
    try:
        cur=mydb.cursor()
        st='create database bank_mgmt'
        cur.execute(st)
        print('Database Successfully created')
    except:
        print('Database Already Exists')
else:
    print('Unable to connect to MySQL')
