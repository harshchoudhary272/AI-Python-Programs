from tkinter import INSERT
from tkinter.tix import InputOnly
import mysql.connector

db = mysql.connector.connect(host = 'localhost', port = 3306, database = 'employee', user = 'root', passwd = 'Harshp272@', charset = 'utf8')


print(db)


# Cursor.execute("CREATE DATABASE EMPLOYEE")
# print("Employee database is created")

# Cursor.execute("CREATE TABLE EMP(name VARCHAR(26), id int)")
# print("Table EMP created"
Cursor = db.cursor()
# query = "INSERT INTO EMP(name,id) VALUES(%s,%s);"

# var = [('Sid', "38"),('Arjun', "5"),('Spiderman', "30")]
# Cursor.executemany(query, var)




# query = "DELETE FROM EMP WHERE name = 'Harsh';"

# Cursor.execute(query)


try:
    print("Before Update :-")
    Cursor.execute("SELECT * FROM EMP")
    myresult = Cursor.fetchall()

    for x in myresult:
        print(x)


    Cursor.execute("UPDATE EMP SET id = '10' WHERE id = '5'")
    db.commit()
    print("After Update :-")
    Cursor.execute("SELECT * FROM EMP")
    myresult = Cursor.fetchall()

    for x in myresult:
        print(x)

except mysql.connector.Error as error:
    print("Exception Caught".format(error))

finally:
    Cursor.close()
    db.close()
    



#print(Cursor.rowcount,'record inserted')

#myresult = Cursor.fetchone()

#print(myresult)



