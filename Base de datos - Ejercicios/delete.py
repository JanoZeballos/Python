import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

sql = "delete from usuarios where id = 22"
cursor.execute(sql)

n_id = int(input("Id: "))

sql = "delete from usuarios where id = %s"
cursor.execute(sql,(n_id,))

sql = "delete from usuarios where id = %s"
registros = [(20,), (21,)]
cursor.executemany(sql, registros)

conexion.commit() 

cursor.close()
conexion.close()
