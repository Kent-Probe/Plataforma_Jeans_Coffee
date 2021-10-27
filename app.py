import os
from datetime import date
from re import T
import re

from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask.scaffold import F
from flask.sessions import SecureCookieSession
from flask.typing import ResponseReturnValue
from markupsafe import escape

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from werkzeug.wrappers.request import PlainRequest
from werkzeug.wrappers.response import ResponseStream

from conexion import accion, seleccion
from forms import Login, comentar, password, plate, profile, search, sign_in

app = Flask(__name__)
app.secret_key = os.urandom(24)


#Manejador de mensajes 400-500
#Pagina 400
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

#Pagina 500
@app.errorhandler(500)
def server_error(e):
    return render_template('error500.html'), 500

#Terminos y condiciones
@app.route("/terms_conditions/")
@app.route("/terminos_condiciones/")
def terms():
    return render_template('terminos.html')

#Pagina de inicio
@app.route("/")
@app.route("/index/")
@app.route("/home/")
@app.route("/principal/")
def index():
    sql = f'SELECT *FROM plato LIMIT 6'
    res = seleccion(sql)

    sql3 = f'SELECT *FROM plato ORDER BY cod_plato DESC LIMIT 3'
    res3 = seleccion(sql3)
    return render_template('index.html', res=res, res3=res3)

#Pagina de inicar sesion
@app.route('/Entrar/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if('user' in session):
        print(session)
        return redirect(url_for('index'))
    else:   
        print(session)
        form = Login()
        if request.method=='GET':
            return render_template('login.html', form=form, titulo='Iniciar sesion')
        else:
            usu = escape(form.name.data.strip())
            pwd = escape(form.password.data.strip())

            sw = True
            if len(usu)<5 or len(usu)>40:
                print("El usuario es requerido, longitud no valida [5-40]")
                sw = False

            if len(pwd)<5 or len(pwd)>40:
                print("la clave es requerido, longitud no valida [5-40]")
                sw = False
            if sw:
                # Preparar la consulta
                sql = f'SELECT contraseña, user, rol FROM usuario WHERE user="{usu}"'
                # Ejecutar la consulta
                res = seleccion(sql)
                # Proceso la respuesta
                if len(res)==0:
                    print('ERROR: Usuario o clave invalidas')
                    return render_template('login.html', form=form, titulo='Iniciar Sesión')
                else:
                    # Recupero el valor de la clave
                    cbd = res[0][0]
                    if check_password_hash(cbd, pwd):
                        session.clear()
                        session['user'] = usu
                        session['contraseña'] = pwd
                        return redirect(url_for('index'))
                    else:
                        print('ERROR: Usuario o clave invalidas')
                        return render_template('login.html', form=form, titulo='Iniciar Sesión')
            else:
                return render_template('login.html', form=form, titulo='Iniciar Sesión')


#Pagina de registrarse
@app.route("/Registrarse/", methods=['GET', 'POST'])
@app.route("/sign_in/", methods=['GET', 'POST'])
def sign():
    form = sign_in()
    if request.method=='GET':
        return render_template('sign_in.html', form=form, titulo='Registro')
    else:
        # Recuperar los datos del formulario
        nom = escape(form.nom.data.strip())
        apl = escape(form.apl.data.strip())
        ema = escape(form.ema.data.strip())
        usr = escape(form.usr.data)
        ads = escape(form.ads.data.strip())
        num = escape(form.num.data)
        cla = escape(form.cla.data)
        ver = escape(form.ver.data)

        # Validar los datos
        sw = True
        if len(nom)<5 or len(nom)>40:
            print("El nombre es requerido, longitud no valida [5-40]")
            sw = False
        if len(apl)<5 or len(apl)>40:
            print("longitud no valida [5-40] para el apellido")
            sw = False
        if len(ema)<5 or len(ema)>40:
            print("El email es requerido, longitud no valida [5-40]")
            sw = False
        if len(usr)<5 or len(usr)>40:
            print("El usuario es requerido, longitud no valida [5-40]")
            sw = False
        if len(ads)<5 or len(ads)>40:
            print("la direccion es requerido, longitud no valida [5-40]")
            sw = False
        if len(cla)<5 or len(cla)>40:
            print("la clave es requerido, longitud no valida [5-40]")
            sw = False
        if ver != cla:
            print("No concuerdan las claves")
            sw = False

        # Ejecutar las acciones a lugar
        if sw:
            # Preparar la consulta
            sql = "INSERT INTO usuario(nombre, apellido, direccion, email, user, contraseña, telefono) VALUES (?, ?, ?, ?, ?, ?, ?)"
            # Ejecutar la consulta
            pwd = generate_password_hash(cla)
            res = accion(sql,(nom, apl, ads, ema, usr, pwd, num))
            print(res)
            # Procesar la respuesta
            if res!=0:
                print('INFO: Datos almacenados con exito')
            else:
                print('ERROR: Por favor reintente')
        return redirect(url_for('login'))
            
#Pagina de favoritos
@app.route("/favoritos/")
@app.route("/favorites/")
def favorites():
    if 'user' in session:
        sql = f"SELECT id_usuario FROM usuario WHERE user='{session['user']}'"
        res = seleccion(sql)

        sql = f"SELECT p.imagen, p.nombre, p.calificacion, p.valor, p.descripcion FROM favoritos f, plato p WHERE f.id_usuario='{res[0][0]}' and p.cod_plato=f.cod_plato"
        res = seleccion(sql)
        
        print(res)
        return render_template('favoritos.html', titulo='favoritos' ,res=res)
    return redirect(url_for('index'))
#Pagina de buscar - Todos los productos
@app.route("/search/")
@app.route("/buscar/")
@app.route("/todos_los_Productos/")
@app.route("/all_product/")
def all_product():
    form = search()
    seh = form.seh.data
    param = request.args.get('seh', seh)
    if param:
        sql = f"SELECT * FROM plato WHERE nombre LIKE '{param}%'"
        res = seleccion(sql)
        return render_template('all_product.html', form=form, titulo='producto', res=res, search=seh)
    else:
        sql = f'SELECT *FROM plato LIMIT 6'
        res = seleccion(sql)
        return render_template('all_product.html', form=form, titulo='producto', res=res, search=seh)

# Pagina de carro de compras seleccion
@app.route("/shopping_car/",methods=['GET', 'POST'])
def shopping_car():
    param = request.args.get('cod_plato')
    if('user' in session):
        if request.method == 'POST':
            if param:
                sql = f"SELECT * FROM compra, usuario u WHERE cod_plato={param} and u.user='{session['user']}'"
                res = seleccion(sql)
                print(res)
                print(not(res))
                if not(res):
                    cantidad = request.form.get('ncantidad')
                    sql = f"INSERT INTO compra(id_usuario, cod_plato, nombre, cantidad, precio, total) SELECT id_usuario, p.cod_plato, p.nombre, {cantidad}, p.valor, {cantidad}*p.valor FROM usuario, plato p WHERE p.cod_plato={param} and user='{session['user']}'"
                    res = seleccion(sql)
        sql = f"SELECT id_compra, nombre, cantidad, precio, total FROM compra WHERE id_usuario=(SELECT id_usuario FROM usuario WHERE user='{session['user']}')"
        resS = seleccion(sql)
        return render_template('shopping_car.html', res = resS)
    else:
        return render_template('shopping_car.html')
        
      
   
# tabla carrito



  
# #delete carrito
@app.route('/delete/')
def delete():
    if 'id_compra' in request.args: 
        id_compra = request.args.get('id_compra')
        sql = f"DELETE FROM compra WHERE id_compra={id_compra}"
        dat = seleccion(sql)
        return redirect(url_for('shopping_car'))
    elif 'id_plato' in request.args:
        cod_plato = request.args.get('id_plato')
        sql = f"DELETE FROM plato WHERE cod_plato={cod_plato}"
        dat = seleccion(sql)
        return redirect(url_for('dashboard'))
    elif 'id_user' in request.args:
        id_usuario = request.args.get('id_user')
        sql = f"DELETE FROM usuario WHERE id_usuario={id_usuario}"
        dat = seleccion(sql)
        return redirect(url_for('usuarios'))
    


# Borrar todos los registros de shopping_car
@app.route('/delete_all/')
def delete_all():
    sql = f"DELETE FROM compra"
    dat = seleccion(sql)
    return redirect(url_for('shopping_car'))
    

#Pagina de producto en especifico
@app.route("/producto/", methods=['GET', 'POST'])
def product():
    param = request.args.get('plate','zumo')
    form = comentar()
    if param:
        sql = f'SELECT * FROM plato WHERE nombre="{param}"'
    else:
        sql = f'SELECT * FROM plato WHERE cod_plato=1'
    res1 = seleccion(sql)
    ideP = res1[0][0]

    sql2 = f"SELECT * FROM comentario WHERE cod_plato={ideP}"
    res2 = seleccion(sql2)
    
    setVal = "no esta"
    
    if 'user' in session:
        sql = f"SELECT id_usuario FROM usuario WHERE user='{ session['user'] }'"
        res = seleccion(sql)
        ideU = res[0][0]

        sql = f"SELECT cod_plato FROM favoritos WHERE cod_plato='{ideP}' and id_usuario='{ideU}'"
        resV = seleccion(sql)

        if resV:
            setVal = "esta"
        if request.method == 'POST':
            if 'favoritos' in request.form:
                if setVal != "esta":
                    sqlf = f"INSERT INTO favoritos(id_usuario, cod_plato) SELECT u.id_usuario, p.cod_plato FROM usuario u, plato p WHERE user='{session['user']}' and cod_plato={ideP}"
                    print(sqlf)
                    res = seleccion(sqlf)
                    print(res)
                    setVal = "esta"
                else:
                    print("Delete of the favorites")
                    sqlD = f"DELETE FROM favoritos WHERE cod_plato={ideP} and id_usuario={ideU}"
                    res = seleccion(sqlD)
                    setVal = "no esta"
                 
            today = date.today()
            coment = form.coment.data
            if coment != "":
                sql = "INSERT INTO comentario(id_usuario, cod_plato, user, comentario, fecha) VALUES(?, ?, ?, ?, ?)"
                res = accion(sql,(ideU, ideP, session['user'], coment, format(today)))
                sql2 = f"SELECT * FROM comentario WHERE cod_plato={ideP}"
                res2 = seleccion(sql2)
                form.coment.data = ""

            #print(res2[1][2] in session['user'])
            if res!=0:
                print('INFO: Datos almacenados con exito')
            else:
                print('ERROR: Por favor reintente')
    else:
        print("Lo siento el usuario no esta en sesion ahora mismo")
    return render_template('product.html', form=form, titulo='producto', res=res1, res2=res2, setVal=setVal)
        
#Pagina de dashboard platos
@app.route('/dashboard/', methods=['GET', 'POST'])
@app.route('/dashboard/platos/', methods=['GET', 'POST'])
def dashboard():
    if 'user' in session:
        form = search()
        if request.method == 'GET':
            sql = f'SELECT *FROM plato'
            res = seleccion(sql)
        else:
            seh = form.seh.data
            param = request.args.get('seh', seh)
            if param:
                sql = f"SELECT * FROM plato WHERE nombre LIKE '{param}%'"
                res = seleccion(sql)
            else:
                sql = f'SELECT *FROM plato'
                res = seleccion(sql)
        return render_template('platos.html', form=form, titulo='dashboard', res=res)
    else:
        return redirect(url_for('index'))

#Pagina de dashboard gestion usuario
@app.route('/dashboard/usuarios/', methods=['GET', 'POST'])
def usuarios():
    if 'user' in session:
        form = search()
        print(request.args.get('cliente'))
        if request.method == 'GET':
            sql = f'SELECT * FROM usuario WHERE id_usuario > 1 '
            res = seleccion(sql)
        else:
            seh = form.seh.data
            param = request.args.get('seh', seh)
            if param:
                sql = f"SELECT * FROM usuario WHERE nombre LIKE '{param}%' and id_usuario > 1"
                res = seleccion(sql)
            else:
                sql = f'SELECT * FROM usuario WHERE id_usuario > 1'
                res = seleccion(sql)
        return render_template('usuarios.html', form=form, titulo='dashboard', res=res)
    else:
        return redirect(url_for('index'))

@app.route('/asignarRol/')
def asignarRol():
    if 'user' in session:
        admin = request.args.get('admin')
        cliente = request.args.get('cliente')
        print(request.args.get('admin'))
        print(request.args.get('cliente'))
        if admin:
            sqlU = f"UPDATE usuario SET rol='admin' WHERE id_usuario={admin}"
            print(sqlU)
            res = seleccion(sqlU)
            return redirect(url_for('usuarios'))
        if cliente:
            sqlU = f"UPDATE usuario SET rol='cliente' WHERE id_usuario={cliente}"
            print(sqlU)
            res = seleccion(sqlU)
            return redirect(url_for('usuarios'))
    else:
        return redirect(url_for('index'))
#Pagina dashboard agregar platos
@app.route('/dashboard/platos/add_plate/', methods=['GET', 'POST'])
@app.route('/dashboard/platos/agregar_plato/', methods=['GET', 'POST'])
def addPlatos():
    if 'user' in session:
        form = plate()
        if request.method=='GET':
            return render_template('add_plate.html', form=form, titulo='Agregar plato')
        else:
            nom = form.nPlato.data.strip()
            val = form.pPlato.data.strip()
            des = form.dPlato.data.strip()

            #Guardar imagen
            f = request.files['aImgPlato']
            nom = secure_filename(f.filename)
            img = f'uploads/{nom}'
            f.save(f'static/{img}')

            # Preparar la consulta
            sql = "INSERT INTO plato(nombre, descripcion, valor, imagen) VALUES (?, ?, ?, ?)"
            # Ejecutar la consulta
            res = accion(sql,( nom, des, val, img))
            #Procesar la respuesta
            if res!=0:
                print('INFO: Datos almacenados con exito')
            else:
                print('ERROR: Por favor reintente')
            return render_template('add_plate.html', form=form, titulo='Agregar plato')
    else:
        return redirect(url_for('index'))

#Pagina dashboard editar plato
@app.route('/dashboard/platos/edit_plate/', methods=['GET', 'POST'])
@app.route('/dashboard/platos/editar_plato/', methods=['GET', 'POST'])
def editPlato():
    if 'user' in session:
        form = plate()
        if request.method=='GET':
            param = request.args.get('id_plato')
            if param:
                sql = f"SELECT * FROM plato WHERE cod_plato='{param}'"
            else:
                sql = "SELECT * FROM plato WHERE cod_plato=1"

            res = seleccion(sql)

            for i in res:
                form.nPlato.data = i[2]
                form.pPlato.data = i[-1]
                form.dPlato.data = i[4]
            return render_template('edit_plate.html', form=form, titulo='Editar plato')
        else:
            nom = form.nPlato.data.strip()
            val = form.pPlato.data.strip()
            des = form.dPlato.data.strip()

            f = request.files['aImgPlato']
            nom = secure_filename(f.filename)
            img = f'uploads/{nom}'
            f.save(f'static/{img}')

            # Preparar la consulta
            sql="UPDATE plato SET nombre=?, descripcion=?, valor=?, img=? WHERE nombre='zumo'"
            # Ejecutar la consulta
            res = accion(sql,( nom, des, val, img))
            print(res)
            print(sql,( nom, des, val, img))
            #Procesar la respuesta
            if res!=0:
                print('INFO: Datos almacenados con exito')
            else:
                print('ERROR: Por favor reintente')
            return render_template('edit_plate.html', form=form, titulo='Editar plato')
    else:
        return redirect(url_for('index'))
#ver perfil
@app.route('/perfil/')
@app.route('/profile/')
def perfil():
    if 'user' in session:
        #Perepar la aconsulta
        sql = f"SELECT * FROM usuario WHERE user= '{session['user']}'"
        print(sql)
        #Ejecuta la consulta
        res = seleccion(sql)
        print(res)
        #Procesar la consulta
        print(res[0][8])
        if 'superadmin' == res[0][8] or 'admin' == res[0][8]:
            return redirect(url_for('dashboard'))
        else:
            return render_template("profile.html", res=res)
    else:
        return redirect(url_for('index'))

#editar Perfil
@app.route('/perfil/editar_perfil/', methods=['GET', 'POST'])
@app.route('/profile/edit_perfil/', methods=['GET', 'POST'])
def editProfile():
    form = profile()
    if 'user' in session:
        if request.method == 'GET':
            #Perepar la aconsulta
            sql = f"SELECT * FROM usuario WHERE user= '{session['user']}'"
            #Ejecuta la consulta
            res = seleccion(sql)
            #Procesar la consulta
            if 'superadmin' == res[0][8] or 'admin' == res[0][8]:
                return redirect(url_for('dashboard'))
            return render_template("edit_profile.html", form = form)
        else:
            #Recuperar datos del formulario
            name = escape(form.nPorfile.data) 
            lName = escape(form.aPellido.data) 
            num = escape(form.num.data) 
            adress = escape(form.adress.data)
            ema = escape(form.ema.data) 
            vema= escape(form.verificarEma.data)
            #Validad datos
            sw = True
            if len(name)<5 or len(name)>40:
                print("El nombre es requerido, longitud no valida [5-40]")
                sw = False
            if len(lName)<5 or len(lName)>40:
                print("longitud no valida [5-40] para el apellido")
                sw = False
            if len(ema)<5 or len(ema)>40:
                print("El email es requerido, longitud no valida [5-40]")
                sw = False
            if ema != ema:
                print("EL email no concuerda")
                sw = False
            if len(adress)<5 or len(adress)>40:
                print("la direccion es requerido, longitud no valida [5-40]")
                sw = False
            if len(num) < 5 or len(num) > 10:
                print("El numero es incorrecto, agrege un numero de Colombia")
                sw = False

            if sw:
                # Ejecutar la consulta
                sql = f"UPDATE usuario SET nombre=?, apellido=?, telefono=?, direccion=?, email=? WHERE user='{session['user']}'"
                res = accion(sql,(name, lName, num, adress, ema))
                #Procesar la respuesta
                if res!=0:
                    print('INFO: Datos almacenados con exito')
                else:
                    print('ERROR: Por favor reintente')
                return render_template("edit_profile.html", form=form)
            else:
                return render_template("edit_profile.html", form=form)
    else:
        return redirect(url_for('index'))

#Cambiar contraseña
@app.route('/profile/change_password/', methods=['GET', 'POST'])
@app.route('/perfil/cambiar_contraseña/', methods=['GET', 'POST'])
def contraseña():
    form = password()
    if 'user' in session:
        if request.method =='GET':
            return render_template("change_passsword.html", form=form)
        else:
            claV = escape(form.claV.data.strip())
            #Perepar la aconsulta
            sql = f"SELECT contraseña FROM usuario WHERE user='{session['user']}'"
            #Ejecuta la consulta
            res = seleccion(sql)
            #Procesar la consulta
            comp = res[0][0]
            if check_password_hash(comp, claV):
                cla = form.cla.data
                ver = form.ver.data
                if cla == ver:
                    # Ejecutar la consulta
                    pwd = generate_password_hash(cla)
                    sql = f"UPDATE usuario SET contraseña='{pwd}' WHERE user='{session['user']}'"
                    res = seleccion(sql)
                    print(sql)
                    print(res)
                    # Procesar la respuesta
                    if res!=0:
                        print('INFO: Datos almacenados con exito')
                    else:
                        print('ERROR: Por favor reintente')
                else:
                    print("Las claves no concuerdan")
            else:
                print("Las clave esta mal escrita")
            return render_template("change_passsword.html", form=form)
    else:
        return redirect('/home')



#metodo para salir ;)
@app.route('/salir/')
def salir():
    print(session)
    session.clear()
    return redirect('/home')


""" @app.after_request
def after_request(response):
    print("ESTA EN EL AFTER")
    if request.endpoint == 'product':
        print("ENTRO EN EL ENDPOINT")
        if 'user' in session:
            if 'favoritos' in request.form:
                print("ENTRO EN FAVORITOS")
                param = request.args.get('plate')
                print(param)
                sqlf = f"INSERT INTO favoritos(id_usuario, cod_plato) SELECT u.id_usuario, p.Plato FROM usuario u, plato p WHERE user='{session['user']} and cod_plato='{param}'"
                res = seleccion(sqlf)
    return response """
    

if __name__ == '__main__':
    app.run(debug=True)
