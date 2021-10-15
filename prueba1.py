import sqlite3
from hashlib import sha512

from werkzeug.security import check_password_hash, generate_password_hash

from conexion import accion

"""
usu = 'Jeans_coffee'
pwd = 'jeansCoffe'


sql = f'INSERT INTO usuario(nombre, apellido, dirreccion, email, user, contraseña) VALUES(mario, will, calle12, mario@gmai.com, mario01, {generate_password_hash(pwd)})'
# Ejecutar la consulta
print(sql)
res = accion(sql)
print(res)

has1 = generate_password_hash('2')
has2 = generate_password_hash('2') 
print(has1)
print(has2)

if check_password_hash(has1,'2'):
    print("Acceso concedido")
else:
    print("Acceso denegado")

if check_password_hash(has2,'2'):
    print("Acceso concedido")
else:
    print("Acceso denegado")

"""

nom = "mario" 
ape = "mario"
adr = "mario"
ema = "mario"
usu = "mario"
 

cla = "carlos01"
# Preparar la consulta
sql = "INSERT INTO USUARIO(nombre, apellido, direccion, email, user, contraseña) VALUEs (?, ?, ?, ?, ?, ?)"
# Ejecutar la consulta
pwd = generate_password_hash(cla)
res = accion(sql,(nom, ape, adr, ema, usu, pwd))
# Procesar la respuesta
if res!=0:
    print('INFO: Datos almacenados con exito')
else:
    print('ERROR: Por favor reintente')