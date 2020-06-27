import pymysql

conn=pymysql.connect(host="localhost",user="root",passwd="",db="project");

myCursor=conn.cursor();
var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")

while var!=-1: 
    if var=="1":
        sql="insert into users(name,age,gender) values(%s,%s,%s)"
        varname=input('please enter the name of the user: ')
        varage=input('please enter his age: ')
        vargender=input('please enter his gender: ')
        val=(varname,varage,vargender)
        myCursor.execute(sql,val)
        print("data inserted")
        conn.commit()
        var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")
 
    if var=="2":
        print("getting all information about users...")
        myCursor.execute("select * from users")
        result=myCursor.fetchall()
        for row in result:
            print(row)
        var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")
     
    if var=="3":
        sql1="select * from users where id=%s"
        x=input("input an id of a user ")
        myCursor.execute(sql1,x)
        result1=myCursor.fetchall()
        for row in result1:
          print(row)
        var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")

    if var=="4":    
        sql2="update users set name=%s where id=%s"
        id1=input("set the id you want to update: ")
        updatedname=input("set the updated name: ")
        myCursor.execute(sql2,(updatedname,id1))
        print("name is updated")
        conn.commit()
        var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")

    if var=="5":
        sql3="delete from users where id=%s"
        id2=input("set the id of the user you want to delete: ")
        myCursor.execute(sql3,id2)
        print("user is deleted")
        conn.commit()
        var=input(" 1 to create a new user,\n 2 to get all information about users,\n 3 to get an information for a specific user,\n 4 to update a user,\n 5 to delete a user,\n -1 to exit: ")
        
else:
    conn.close()



