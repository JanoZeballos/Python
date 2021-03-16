import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

sql = "select usuario, clave from usuarios where id = 2"
cursor.execute(sql)

resultado = cursor.fetchone()
print (resultado)

sql = "select usuario, clave from usuarios where id = %s"
cursor.execute(sql,(1,))

resultado = cursor.fetchone()
print (resultado)
