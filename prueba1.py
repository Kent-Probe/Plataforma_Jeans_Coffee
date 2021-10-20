

from conexion import seleccion, accion

ide = 0

sql = f'SELECT *FROM plato LIMIT 6'
res = seleccion(sql)
for i in res:
    print(res)


    



#sql = "SELECT * FROM plato WHERE nombre= 'nombre'"
#
#res = seleccion(sql)
#for i in res:
#    print("nombre: ",i[2])
#    print("descipcion: ",i[4])
#    print("valor?: ",i[-1])
#    print()
#
#sql="UPDATE plato SET nombre=?, descripcion=?,valor=? WHERE nombre='nombre'"
## Ejecutar la consulta
#res = accion(sql,( 'nombre', 'des', '23333'))
