import mysql.connector      # conector para mysql
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect)
cursor = conexion.cursor()

sql = "select * from usuarios"

cursor.execute(sql)

resultados = cursor.fetchall()

# print(resultados) 

print("Nombre\tClave")
for datos in resultados:
    print (datos[1],'\t',datos[2])

conexion.close()