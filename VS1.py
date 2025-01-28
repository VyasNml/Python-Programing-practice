import time
print ("\t\t\t",time.ctime())


import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
mycursor=conn.cursor()


conn.autocommit = True
def Create():
    mycursor.execute("use vyas")
    mycursor.execute("create table log_id(user_id varchar(20) ,password  varchar(100) primary key)")
    mycursor.execute("create table OFFICE (em_no bigint,em_name varchar(255),em_dept varchar(255),em_salary int,em_age int)")
    mycursor.execute("create table em_performance (em_no bigint,em_name varchar(255),em_dept varchar(255),em_performance varchar(255),em_work varchar(255))")




   
def menu():
    print("=============== EMPLOYEES MANAGEMENT SYSTEM ================")
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
        print(" ")
        print(" 1.employee registeration")
        print(" 2.employee details")
        print(" 3.update salary")
        print(" 4.employees list")
        print(" 5.know the number of employees")
        print(" 6.work experience")
        print(" 7.know your salary")
        print(" 8.exit")
        choice=int(input(" enter the choice:"))       
        
        if choice==1:
            register()
        elif choice==2:
            details()
        elif choice==3:
            em_salary()
        elif choice==4:
            em_list()
        elif choice==5:
            em_count()
        elif choice==6:
            em_perform()
        elif choice==7:
            salary()
        else:
            
            print("=========Thank You==========")
            break
    else : print("==========Thank You===========")
    
def register():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
    mycursor=conn.cursor()
    v_em_no=int(input("enter your employee ID :"))
    v_em_name=input ("enter your name :")
    v_em_dept=input( "enter department you want to join : ")
    v_em_salary=input ("enter your salary :")
    v_em_age=int(input("enter your age :"))
    v_sql_insert="insert into office values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"',"+str(v_em_salary)+","+str(v_em_age)+")"
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("congrats you have joined suuceessfully")
    print("       registerd successfully          ")


def details():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
    mycursor=conn.cursor()
    mycursor.execute("select* from OFFICE")
    results=mycursor.fetchall()
    conn.commit()
    for x in results:
        print(x)




def em_salary():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
    mycursor=conn.cursor()
    nam=input("enter your name")
    mycursor.execute("update office set em_salary=em_salary+em_salary*10/100 where em_name='{}'".format(nam))
    print("     Updated Successfully")
    conn.commit()
   
def em_list():
    import mysql.connector as sql
    try:
        conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
        mycursor=conn.cursor()
        mycursor.execute("select em_name from office order by em_name asc")
        list_=mycursor.fetchall()
        for x in list_:
            print (x)
        a=mycursor.rowcount()
        print("total employees are",a)
    except:
        print ("unable to show the list")


def em_count():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='root',database='vyas')
    mycursor=conn.cursor()
    mycursor.execute("select count(distinct em_name) from office")
    count=mycursor.fetchall()
    for x in count:
        print("    numbr of employees:",x)
    conn.commit()


def salary():
    nam=input("enter your name :")
    a=mycursor.execute("select em_salary from office where em_name='{}'".format(nam))
    mycursor.execute(a)
    salary=mycursor.fetchall()
    for x in salary:
        print(        x,"is your current salary",nam       )
    conn.commit()


def em_perform():
    v_em_no=int(input("enter your employee ID"))
    v_em_name=input ("enter your name:")
    v_em_dept=input( "enter department you want to join : ")
    v_em_performance=input("enter your performance:") 
    v_em_work=input ("enter your experience(YEARS):")
    v_sql_insert="insert into em_performance values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"','"+v_em_performance+"',"+str(v_em_work)+")"
    print(v_sql_insert)
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("performance added")
   
Create()
menu()  



