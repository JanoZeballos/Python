import mysql.connector
import datos_db

conexion = mysql.connector.connect(**datos_db.dbConnect2)
cursor = conexion.cursor()

sql = "select * from inventario limit 25"   # cuantos registros queres ver
cursor.execute(sql)
resultados = cursor.fetchall()

print("Codigo\tModelo\Stock")
for datos in resultados:
    print (datos[1],'\t',datos[2],'\t',datos[3])


cantidad = "select count(*) from inventario"
cursor.execute(cantidad)
resultado = cursor.fetchone()
print (resultado)   # la cantidad de registros

sql = "select * from inventario"  
cursor.execute(sql)
resultados = cursor.fetchall()   # la lista de productos

i = 1
while i < resultado[0]:
    print (i,'\t',
    resultados[i][1],'\t',resultados[i][2],'\t',resultados[i][3])
    i=i+1
    if i % 25 == 0:     # multiplo de 25
        espera = input("Presione enter para continuar")


sql = "select * from inventario where modelo like '%espuma%'"  # dentro del like no hay diferencia entre min y may
cursor.execute(sql)
resultados = cursor.fetchall()

print(resultados)

conexion.close()