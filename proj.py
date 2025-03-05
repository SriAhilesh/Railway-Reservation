import mysql.connector as ms 
Ags=ms.connect(host='localhost',user='root',password='SPLofKSV@1218',database='success') 
Cursor1=Ags.cursor() 
S2 = "CREATE TABLE IF NOT EXISTS railway (name VARCHAR(100), phone INT(30) NOT NULL, age INT(3), gender VARCHAR(10), No_of_tickets INT(20), from_f VARCHAR(100), to_t VARCHAR(100), date_d VARCHAR(100))"
Cursor1.execute(S2)

S3 = "CREATE TABLE IF NOT EXISTS user_accounts (firstname VARCHAR(20), lastname VARCHAR(20), username VARCHAR(40), password VARCHAR(10) PRIMARY KEY, phonenumber INT(30), gender VARCHAR(10), date_of_birth VARCHAR(20))"
Cursor1.execute(S3)  

 
def Signin(): 
        firstname=input("enter your fname") 
        lastname=input("enter your lname") 
        username=input("enter your username") 
        password=input("enter the password") 
        phonenumber=int(input("enter your phonenumber")) 
        gender=input("gender") 
        date_of_birth=input("enter your dob") 
        Cursor1.execute("insert into user_accounts values('{}','{}','{}','{}',{},'{}','{}')".format (firstname,lastname,username,password,phonenumber,gender,date_of_birth))  
 
        Ags.commit 
        print("your account has been Created successfully") 
        z=Menu() 
        return z 
 
def login(): 
       a=input('enter the username ') 
       b=input('enter the password') 
       S6="select username,firstname,lastname from user_accounts where password='{}'".format(b)  
        
       Cursor1.execute(S6)  
       data1=Cursor1.fetchone() 
 
       if data1: 
          Data1=list(data1) 
          print('HI',Data1[1]) 
          print("You Have logged in successfully") 
       else: 
          print("Accound does not exist") 
       X=Menu() 
       return X 
 
def Delete(): 
 
       a=input("enter username") 
       b=input("enter password") 
       Cursor1.execute("delete from user_accounts where password='{}'".format(b)) 
 
       print("ACCOUNT DELETED SUCCESSFULLY") 
       Ags.commit() 
       return 'y' 
 
 
def Menu(): 
       print("1.YES") 
       print("2.NO") 
       c=int(input("Do you want to continue")) 
       while c==1: 
          print("1.TICKET BOOKING") 
          print("2.TICKET CHECKING") 
          print("3.TICKRT CANCELLING") 
          print("4.LOG OUT") 
          ch=int(input("Enter your choice")) 
          if ch==1: 
             Book_tickets() 
          if ch==2: 
             check_tickets() 
          if ch==3: 
             cancel_tickets() 
          if ch==4: 
             print("THANK YOU") 
             return 'y'  
       else: 
            print("ERROR 404 PAGE NOT FOUND")  
 
def Book_tickets(): 
       name=input("enter your name") 
       phone=int(input("enter your phone number")) 
       age=int(input("Enter your age")) 
       #print('M=Male','\n','F=Female','\n','N=Not to mention') 
       gender=input("Enter gender")  
       No_of_tickets=int(input("Enter number of tickets")) 
       from_f=input("Enter starting point") 
       to_t=input("Enter your destination") 
       date=input("Enter the date you want to travel ") 
       Cursor1.execute("insert into railway values('{}',{},{},'{}',{},'{}','{}','{}')".format(name,phone,age,gender,No_of_tickets,from_f,to_t,date)) 
       Ags.commit() 
       print("TICKETS BOOKED SUCCESSFULLY")  
 
def check_tickets(): 
       Pho=int(input("enter your phone number ")) 
       Cursor1.execute("select * from railway where phone={}".format(Pho)) 
       data=Cursor1.fetchall() 
       if data: 
          print() 
          print("\t\tBOOKING DETAILS") 
          print("\t\t******** ******") 
          a=['NAME     ','PHONENUMBER      ','AGE    ','GENDER   ','NO OF TICKETS    ','STARTING POINT    ','DESTINATION','DATE    '] 
          Data=list(data) 
          K=0 
          for I in Data: 
            for j in I: 
                print(a[K],":::::::::::::",j) 
                K+=1 
       else: 
          print("YOU DONT HAVE A BOOKING")  
 
def cancel_tickets(): 
       pho=int(input("enter your phone number")) 
       Cursor1.execute("delete from railway where phone={}".format(pho)) 
       print("TICKETS CANCELLED")  
 
#MAINPROGRAM 
ans='y' 
while ans=='y': 
    print() 
    print("="*80) 
    print("WELCOME TO RAILWAY RESERVATION") 
    print("="*80) 
    print() 
    print("1.TO CREATE AN ACCOUNT") 
    print("2.ALREADY A USER ? LOGIN") 
    print("3.TO DELETE AN EXISTING ACCOUNT ") 
    ch1=int(input("enter your choice")) 
    if ch1==1: 
       ans=Signin() 
    if ch1==2: 
       ans=login() 
    if ch1==3: 
       ans=Delete() 
    else: 
        break
