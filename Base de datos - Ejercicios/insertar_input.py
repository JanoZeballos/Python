import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

cursor = conexion.cursor()

nom = input("Nombre usuario: ")
clave = input("Clave usuario: ")
rol_id = int(input("Rol: "))

sqlInsertar = "insert into usuarios(id,usuario,clave,rol_id) values(%s,%s,%s,%s)"
cursor.execute(sqlInsertar, ('null', nom, clave, rol_id))

sqlInsertar = "insert into usuarios(id,usuario,clave,rol_id) values(%s,%s,%s,%s)"
registros = [('null',"pepa","eef546",2,), ('null',"esteban","twbh778",1,), ('null',"ale","ambr43",3,)]
cursor.executemany(sqlInsertar, registros)

conexion.commit()  

cursor.close()
conexion.close()