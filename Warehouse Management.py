import mysql.connector as mys
usern=input("Enter the username: ")
password=input("Enter the password: ")
print("1 - Existing user, 2 - New user")
c=int(input("Enter your choice: "))
if c==2:
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("show databases")
    myc.execute("create database Warehouse")
    myc.execute("create database War_users")
    myc.execute("use Warehouse")
    myc.execute("create table Items(INo varchar(10) primary key, IName varchar(40), Category varchar(20), Quantity integer(10), Price integer(15))")
    myc.execute("create table emp(ENo varchar(10) primary key, EName varchar(40),Gender varchar(10), Dept varchar(20), Doj date, Salary integer(15))")
    myc.close()
    mydb.close()

#Functions for Item_management
def Add_item():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    while True:
        Iid=input("Enter the id of the item: ")
        In=input("Enter the name of the item: ")
        C=input("Enter the category of the item (Book,Fashion,Toy,Electronics,Furniture,Grocery): ")
        Q=int(input("Enter the quantity of the item: "))
        P=int(input("Enter the cost of the item: "))
        qry="insert into Items values('{0}','{1}','{2}',{3},{4})".format(Iid,In,C,Q,P)
        myc.execute(qry)
        mydb.commit()
        ch=input("Do you want to add more? (Y/N): ")
        if ch=="N":
            break
    myc.close()
    mydb.close()

def Delete_item():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    Iid=input("Enter the id of the item to be removed: ")
    myc.execute("delete from Items where INo='{}'".format(Iid))
    mydb.commit()
    myc.close()
    mydb.close()

def Update_item():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    Iid=input("Enter the id of the item whose details has to be updated: ")
    nou=int(input("Enter the number of fields to be updated: "))
    while nou>0:
        f=input("Enter the field to be updated (INo=i, IName=n, Category=c, Quantity=q, Price=p): ")
        if f=="i":
            nv=input("Enter the new value: ")
            qry="update Items set INo='{0}' where INo='{1}'".format(nv,Iid)
            myc.execute(qry)
            mydb.commit()
        elif f=="n":
            nv=input("Enter the new value: ")
            qry="update Items set IName='{0}' where INo='{1}'".format(nv,Iid)
            myc.execute(qry)
            mydb.commit()
        elif f=="c":
            nv=input("Enter the new value: ")
            qry="update Items set Category='{0}' where INo='{1}'".format(nv,Iid)
            myc.execute(qry)
            mydb.commit()
        elif f=="q":
            nv=int(input("Enter the new value: "))
            qry="update Items set Quantity='{0}' where INo='{1}'".format(nv,Iid)
            myc.execute(qry)
            mydb.commit()
        elif f=="p":
            nv=int(input("Enter the new value: "))
            qry="update Items set Price='{0}' where INo='{1}'".format(nv,Iid)
            myc.execute(qry)
            mydb.commit()
        else:
            print("Please enter a valid choice.")
        nou=nou-1
    myc.close()
    mydb.close()

def Display_items_m():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    myc.execute("select * from Items")
    print("INo","\t","IName","\t","Category","\t","Quantity","\t","Price")
    for i in myc:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    myc.close()
    mydb.close()
    
            
#Functions for Employee_management
def Add_emp():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    while True:
        Eid=input("Enter the id of the employee: ")
        En=input("Enter the name of the employee: ")
        G=input("Enter the gender of the employee: ")
        D=input("Enter the department of the employee: ")
        Do=input("Enter the date of joining of the employee (yyyy-mm-dd): ")
        S=int(input("Enter the salary of the employee: "))
        qry="insert into emp values('{0}','{1}','{2}','{3}','{4}',{5})".format(Eid,En,G,D,Do,S)
        myc.execute(qry)
        mydb.commit()
        ch=input("Do you want to add more? (Y/N): ")
        if ch=="N":
            break
    myc.close()
    mydb.close()


def Delete_emp():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    Eid=input("Enter the id of the employee to be removed: ")
    myc.execute("delete from emp where ENo='{}'".format(Eid))
    mydb.commit()
    myc.close()
    mydb.close()

def Update_emp():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    Eid=input("Enter the id of the employee whose details has to be updated: ")
    nou=int(input("Enter the number of fields to be updated: "))
    while nou>0:
        f=input("Enter the field to be updated (ENo=i, EName=n, Gender=g, Dept=d, Doj=do, Salary=s): ")
        if f=="i":
            nv=input("Enter the new value: ")
            qry="update emp set ENo='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        elif f=="n":
            nv=input("Enter the new value: ")
            qry="update emp set EName='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        elif f=="g":
            nv=input("Enter the new value: ")
            qry="update emp set Gender='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        elif f=="d":
            nv=input("Enter the new value: ")
            qry="update emp set Dept='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        elif f=="do":
            nv=input("Enter the new value(yyyy-mm-dd): ")
            qry="update emp set Doj='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        elif f=="s":
            nv=int(input("Enter the new value: "))
            qry="update emp set Salary='{0}' where ENo='{1}'".format(nv,Eid)
            myc.execute(qry)
            mydb.commit()
        else:
            print("Please enter a valid choice.")
        nou=nou-1
    myc.close()
    mydb.close()


def Display_emps():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    myc.execute("select * from emp")
    print("ENo","\t","EName","\t","Gender","\t","Dept","\t","Doj","\t","Salary")
    for i in myc:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
    myc.close()
    mydb.close()


#Functions for user
def Display_items_u():
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use Warehouse")
    print("Which category do you want to explore? (Books=b, Fashion=f, Toys=t, Electronics=e, Furniture=fu, Groceries=g)")
    ch=input("Enter your choice: ")
    d={"b":"Book","f":"Fashion","t":"Toy","e":"Electronics","fu":"Furniture","g":"Grocery"}
    print("Item_No","\t","Name","\t","Price")
    qry="select INo,IName,Price from Items where Category='{}'".format(d[ch])
    myc.execute(qry)
    for i in myc:
        print(i[0],"\t",i[1],"\t",i[2])
    myc.close()
    mydb.close()

def Place_order(i,da):
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use War_users")
    myc.execute("show tables")
    t=[]
    print(i)
    for k in myc:
        for j in k:
            t.append(j)
    if i not in t:
        myc.execute("use Warehouse")
        Iid=input("Enter the id of the item you need to purchase: ")
        qu=int(input("Enter the quantity: "))
        myc.execute("select * from Items where INo='{}'".format(Iid))
        d=[]
        for l in myc:
            for j in l:
                d.append(j)
        if d[4]==0:
            print("The item is not available.")
        elif (d[4]-qu)<0:
            print("The item is not available.")
        else:
            print("Your total cost is: ",qu*d[4])
            myc.execute("update Items set Quantity=Quantity-{0} where INo='{1}'".format(qu,Iid))
            mydb.commit()
            dat=[d[0],d[1],d[2],qu,d[4],da]
            Create_tab_u(i,dat)
    else:
        myc.execute("use Warehouse")
        Iid=input("Enter the id of the item you need to purchase: ")
        qu=int(input("Enter the quantity: "))
        myc.execute("select * from Items where INo='{}'".format(Iid))
        d=[]
        for l in myc:
            for j in l:
                d.append(j)
        print("Your total cost is: ",qu*d[4])
        myc.execute("update Items set Quantity=Quantity-{0} where INo='{1}'".format(qu,Iid))
        mydb.commit()
        dat=[d[0],d[1],d[2],qu,d[4],da]
        add_entry(i,dat)
    myc.close()
    mydb.close()
        
def Create_tab_u(idu,dta):
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use War_users")
    qry="create table {}(INo varchar(8),IName varchar(40),Category varchar(20), Quantity integer(10), Price integer(15), Dop date)".format(idu)
    myc.execute(qry)
    qry2="insert into {0} values('{1}','{2}','{3}',{4},{5},'{6}')".format(idu,dta[0],dta[1],dta[2],dta[3],dta[4],dta[5])
    myc.execute(qry2)
    mydb.commit()
    myc.close()
    mydb.close()
    print(dta)
    
def add_entry(idu,dta):
    mydb=mys.connect(host="localhost",user=usern,passwd=password,database="War_users")
    myc=mydb.cursor()
    qry="insert into {0} values('{1}','{2}','{3}',{4},{5},'{6}')".format(idu,dta[0],dta[1],dta[2],dta[3],dta[4],dta[5])
    myc.execute(qry)
    mydb.commit()
    myc.close()
    mydb.close()

def Past_activities(i):
    mydb=mys.connect(host="localhost",user=usern,passwd=password)
    myc=mydb.cursor()
    myc.execute("use War_users")
    myc.execute("select * from {}".format(i))
    print("INo","\t","IName","\t","Category","\t","Quantity","\t","Price","\t","Dop")
    for i in myc:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
    myc.close()
    mydb.close()


#Functions for manager
def Item_management():
    while True:
        print("__Main menu__")
        print("1. Add items.")
        print("2. Remove an item.")
        print("3. Modify an item.")
        print("4. Display all items.")
        print("5. Exit")
        cho=int(input("Enter your choice: "))
        if cho==1:
            Add_item()
        elif cho==2:
            Delete_item()
        elif cho==3:
            Update_item()
        elif cho==4:
            Display_items_m()
        elif cho==5:
            break
        else:
            print("Please enter a valid choice.")

def  Employee_mangement():
    while True:
        print("__Main menu__")
        print("1. Add employees.")
        print("2. Remove existing employee.")
        print("3. Modify details of an employee.")
        print("4. Display all employee details.")
        print("5. Exit")
        cho=int(input("Enter your choice: "))
        if cho==1:
            Add_emp()
        elif cho==2:
            Delete_emp()
        elif cho==3:
            Update_emp()
        elif cho==4:
            Display_emps()
        elif cho==5:
            break
        else:
            print("Please enter a valid choice.")
    
        
#Main
print("Welcome to the warehouse.")
ch=input("Are you a user or manager? (user=u/manager=m): ")
if ch=="u":
    ui=input("Enter the user_id: ")
    da=input("Enter today's date (yyyy-mm--dd): ")
    while True:
        print("__Main menu__")
        print("1. Display all items.")
        print("2. Place order.")
        print("3. Display past activities.")
        print("4. Exit")
        cho=int(input("Enter your choice: "))
        if cho==1:
            Display_items_u()
        elif cho==2:
            Place_order(ui,da)
        elif cho==3:
            Past_activities(ui)
        elif cho==4:
            print("Thanks for visiting.")
            break
        else:
            print("Please enter a valid choice.")
        
    
elif ch=="m":
    while True:
        print("__Main menu__")
        print("1. Item management.")
        print("2. Employee management")
        print("3. Exit")
        cho=int(input("Enter your choice: "))
        if cho==1:
            Item_management()
        elif cho==2:
            Employee_mangement()
        elif cho==3:
            print("Thanks for visiting.")
            break
        else:
            print("Please enter a valid choice.")
            
        
        
