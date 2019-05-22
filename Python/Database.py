import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='mydb',
    auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()


def intsertData(reloj, temp, humid):
    sql = "INSERT INTO eventos (Hora, Temperatura, Humedad) VALUES (%s, %s, %s)"
    val = (reloj, temp, humid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
