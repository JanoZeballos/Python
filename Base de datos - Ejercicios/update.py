import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

sql = "update usuarios set clave = 'solgty780' where id = 27"
cursor.execute(sql)

'''n_id = int(input("Id: "))
clave = input("Clave usuario: ")

sql = "update usuarios set clave = %s where id = %s"
cursor.execute(sql, (clave, n_id,))'''

conexion.commit() 

cursor.close()
conexion.close()
