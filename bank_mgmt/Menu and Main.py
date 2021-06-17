from prettytable import PrettyTable
import mysql.connector as sqltor
import random
bankdb=sqltor.connect(host='localhost',user='root',passwd='123456',database='bank_mgmt',charset='utf8')
cursor=bankdb.cursor()
print("\t**********************")
print("\tBANK MANAGEMENT SYSTEM")
print("\t**********************")
print("\tCreated By:")
print("\tDeepanshu Anand")
print('\n\n')
def drawtable():
    table=PrettyTable()
    table.field_names=['ACC_NO','HOLDER_NAME','ACC_TYPE','BALANCE','AADHAR_NO']
    cursor.execute('select * from bank')
    data=cursor.fetchall()
    for row in data:
        table.add_row(list(row))
    print(table)

def display(a):
    table=PrettyTable()
    table.field_names=['ACC_NO','HOLDER_NAME','ACC_TYPE','BALANCE','AADHAR_NO']
    cursor.execute('select * from bank where acc_no=%s',(a,))
    data=cursor.fetchall()
    for row in data:
        table.add_row(list(row))
    print(table)

def check():
    lst=list()
    cursor.execute('select * from bank')
    data=cursor.fetchall()
    for row in data:
        lst.append(row[0])
    return lst

def adhar():
    lst1=list()
    cursor.execute('select * from bank')
    data=cursor.fetchall()
    for row in data:
        lst1.append(row[4])
    return lst1
        
def add_acc(a,b,c,d,e):
    st='''insert into bank
    values(%s,%s,%s,%s,%s)'''
    values=(a,b,c,d,e)
    cursor.execute(st,values)
    bankdb.commit()

def show(a):
    cursor.execute('select * from bank where acc_no=%s',(a,))
    data=cursor.fetchall()
    for row in data:
        return row

def deposit(a,b):
    st='update bank set balance=balance+%s where acc_no=%s'
    data=(b,a)
    cursor.execute(st,data)
    bankdb.commit()
    return cursor.rowcount

def withdraw(a,b):
    st='update bank set balance=balance-%s where acc_no=%s'
    data=(b,a)
    cursor.execute(st,data)
    bankdb.commit()
    return cursor.rowcount

def balance(a):
    st='select * from bank where acc_no=%s'
    data=(a,)
    cursor.execute(st,data)
    data=cursor.fetchone()
    return data[3]

def acctype(a):
    cursor.execute('select * from bank where acc_no=%s',(a,))
    data=cursor.fetchone()
    return data[2]

def delete(a):
    st='delete from bank where acc_no=%s'
    data=(a,)
    cursor.execute(st,data)
    bankdb.commit()
    return cursor.rowcount
#--------------------------------------_main_----------------------------------#
while True:
    print("\tMAIN MENU")
    print("\t1. OPEN NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. CLOSE AN ACCOUNT")
    print("\t6. VIEW ALL ACCOUNTS(ADMINS ONLY)")
    print("\t7. EXIT")
    print("Enter your choice (1-7) ")
    ch = input()
   
    if ch=='1':
        print('Welcome To XYZ bank\nEnter necessary details') 
        num=random.randint(1001,9999)
        numlist=check()
        while num in numlist:
            num=random.randint(1001,9999)
        name=input('Enter Account holder name:').upper()
        while name=='':
            print('Empty Field Encountered Try Again')
            name=input('Enter Account holder name:').upper()
        adh=int(input('Enter your AADHAR CARD NO.:'))
        adhr=adhar()
        while adh in adhr:
            print('This Adhaar number already exists. Enter valid Adhaar number')
            adh=int(input('Enter your AADHAR CARD NO.:'))
        while len(str(adh)) != 12:
            print('The adhaar number must be of 12 digits')
            adh=int(input('Enter your AADHAR CARD NO.:'))
        typ=input('Enter acc type (S-for Saving Acc|C-for Current Acc):').upper()
        if typ=='S':
            bal=1000
            add_acc(num,name,typ,bal,adh)
            detail=show(num)
            display(num)
            print('\tAccount Created Successfully')
            print('-------------------------------RESTART--------------------------------------')
        elif typ=='C':
            bal=5000
            add_acc(num,name,typ,bal,adh)
            detail=show(num)
            display(num)
            print('\tAccount Created Successfully')
            print('-------------------------------RESTART--------------------------------------')
        else:
            print('Invalid Input or Empty Field\n--------Try Again--------')

    elif ch=='2':
        num=int(input('Enter account number:'))
        numlist=check()
        while num not in numlist:
            print('This account donot exist.')
            num=int(input('Enter valid account number:'))
        amt=int(input('Enter amount to be deposited:'))
        count=deposit(num,amt)
        if count==0:
            print('-------------------------------RESTART--------------------------------------')
        else:
            print('\tAmount added successfully')
            print('-------------------------------RESTART--------------------------------------')

    elif ch=='3':
        num=int(input('Enter account number:'))
        numlist=check()
        while num not in numlist:
            print('This account donot exist.')
            num=int(input('Enter valid account number:'))
        bal=balance(num)
        typ=acctype(num)
        if typ=='S' and bal>1000:
            amt=int(input('Enter amount to withdraw:'))
            if amt>=bal or (bal-amt)<1000:
                print('Minimum balance must be maintained\ncannot make transaction')
                print('-------------------------------RESTART--------------------------------------')
            else:
                count=withdraw(num,amt)
                if count==0:
                    print('-------------------------------RESTART--------------------------------------')
                else:
                    print('\tAmount debited successfully')
                    print('-------------------------------RESTART--------------------------------------')
        elif typ=='C' and bal>5000:
            amt=int(input('Enter amount to withdraw:'))
            if amt>=bal or (bal-amt)<5000:
                print('Minimum balance must be maintained\ncannot make transaction')
                print('-------------------------------RESTART--------------------------------------')
            else:
                count=withdraw(num,amt)
                if count==0:
                    print('-------------------------------RESTART--------------------------------------')
                else:
                    print('\tAmount debited successfully')
                    print('-------------------------------RESTART--------------------------------------')                                
        else:
            print('Minimum balance reached cannot make transaction.')

    elif ch=='4':
        num=int(input('Enter account number:'))
        numlist=check()
        while num not in numlist:
            print('This account donot exist.')
            num=int(input('Enter valid account number:'))
        display(num)
        print('-------------------------------RESTART--------------------------------------')
 
    elif ch=='5':
        num=int(input('Enter account number:'))
        count=delete(num)
        if count==0:
            print('The account donot exist\nPlease try again')
            print('-------------------------------RESTART--------------------------------------')
            
        else:
            print('\tAccount deleted successfully')
            print('-------------------------------RESTART--------------------------------------')
                
    elif ch=='6':
        pin=input('Enter Admin password:')  #admin password=bkmgmt2020
        if pin=='bkmgmt2020':           
            drawtable()
            print('-------------------------------RESTART--------------------------------------')
                
        else:
            print('Authentication failed')
            print('-------------------------------RESTART--------------------------------------')
    elif ch=='7':
        print('Thank you for using this system')
        break

    else:
        print('You entered an invalid choice')
        print('-------------------------------RESTART--------------------------------------')       
