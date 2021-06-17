import mysql.connector as sqltor
mydb=sqltor.connect(host='localhost',user='root',password='123456',database='bank_mgmt',charset='utf8')
if mydb.is_connected():
    try:
        cur=mydb.cursor()
        st='''create table bank
        (ACC_NO int primary key,
        HOLDER_NAME varchar(20) not null,
        ACC_TYPE char(1) not null,
        BALANCE decimal(10,2) not null,
        AADHAR_NO bigint not null unique)'''
        cur.execute(st)
        mydb.commit()
    except:
        print('Table Aready Exists')
        
else:
    print('UNABLE TO CONNECT TO DATABASE')
mydb.close()
