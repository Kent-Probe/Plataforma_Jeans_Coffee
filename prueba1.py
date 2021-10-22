import os

from flask import Flask, session
from flask.sessions import SessionInterface

app = Flask(__name__)

app.secret_key = os.urandom(24)

session = SessionInterface()

@app.route('/set/<value>')
def set_sesion(value):
    session['value'] = value
    return f'El valor es {value}'

@app.route('/get')
def get_session():
    return f'El valor en la sesion es { session.get("value") }'


""" sql = "SELECT contraseña, user, rol FROM usuario WHERE user='jeanCoffee'"
# Ejecutar la consulta
res = seleccion(sql)
print("Query")
print(res)
print(res[0][0])
print(res[0][1])
print(res[0][2])
# Proceso la respuesta
# Recupero el valor de la clave
print("valores de las sesiones:")
print("valores de las sesiones:") """


print(session)















#ide = 0

#sql = f'SELECT *FROM plato LIMIT 6'
#res = seleccion(sql)
#for i in res:
#    print(res)
""" 
pwd = generate_password_hash('superadmin')
sql = f"UPDATE usuario SET contraseña='{pwd}' WHERE rol='superadmin'"
print(sql) """
# Ejecutar la consulta
#res = accion(sql,(pwd))
    



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
