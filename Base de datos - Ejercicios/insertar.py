import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

sqlInsertar = "insert into usuarios(id,usuario,clave,rol_id) values('null', 'juan', 'jp45t$', '2')"
cursor.execute(sqlInsertar)

conexion.commit()  

print(cursor.rowcount, "regitro(s) insertado")  # cantidad de registros insertados

cursor.close()
conexion.close()
