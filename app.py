from flask import Flask, render_template, request, session, flash
from markupsafe import escape
from wtforms import form
from forms import Login, sign_in, search, comentar, plate, profile, password
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Pagina de inicio
@app.route("/Principal/")
@app.route("/home/")
@app.route("/index/")
@app.route("/")
def index():

    return render_template('index.html', usuario = 'name')

#Pagina de inicar sesion
@app.route('/Entrar/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method=='GET':
        return render_template('login.html', form=form, titulo='Ingresar')
    else:
        # 1. Recuperar los datos del formulario y le aplico transformaciones
        name = form.name.data.strip()
        password = form.password.data.strip()
        # 2. Validar
        sw = True
        if len(name)<5 or len(name)>40:
            flash("El nombre de usuario es requerido, longitud no valida [5-40]")
            sw = False
        if len(password)<5 or len(password)>40:
            flash("El password es requerido, longitud no valida [5-40]")
            sw = False
        # 3. Ejecutar la acción
        if sw and name=='pedro' and password=='pedro':
            session['usuario'] = name
            session['clave'] = password
            return render_template("index.html")
        else:
            flash("Usuario o contraseña no validos")
            return render_template('login.html', form=form, titulo='Ingresar')

#Pagina de registrarse
@app.route("/Registrarse/",methods=['GET', 'POST'])
@app.route("/sign_in/", methods=['GET', 'POST'])
def sign():
    form = sign_in()
    if request.method=='GET':
        return render_template('sign_in.html', form=form, titulo='Registro')
    else:
        # Recuperar los datos del formulario
        nom = form.nom.data.strip()
        apl = form.apl.data.strip()
        ema = form.ema.data.strip()
        usr = form.usr.data.strip()
        ads = form.ads.data.strip()
        num = form.num.data
        cla = form.cla.data.strip()
        ver = form.ver.data.strip()

        # Validar los datos
        sw = True
        if len(nom)<5 or len(nom)>40:
            flash("El nombre es requerido, longitud no valida [5-40]")
            sw = False
        if len(apl)<5 or len(apl)>40:
            flash("longitud no valida [5-40] para el apellido")
            sw = False
        if len(ema)<5 or len(ema)>40:
            flash("El email es requerido, longitud no valida [5-40]")
            sw = False
        if len(usr)<5 or len(usr)>40:
            flash("El usuario es requerido, longitud no valida [5-40]")
            sw = False
        if len(ads)<5 or len(ads)>40:
            flash("la direccion es requerido, longitud no valida [5-40]")
            sw = False
        if len(cla)<5 or len(cla)>40:
            flash("la clave es requerido, longitud no valida [5-40]")
            sw = False
        if ver != cla:
            flash("No concuerdan las claves")
            sw = False

        # Ejecutar las acciones a lugar
        if sw:
            return render_template('index.html')

#Pagina de usuario
@app.route("/usuario/")
@app.route("/username/")
def username():
    return render_template('usuarios.html', titulo='usuario')

#Pagina de favoritos
@app.route("/favoritos/")
@app.route("/favorites/")
def favorites():
    return render_template('favoritos.html', titulo='favoritos')

#Pagina de buscar - Todos los productos
@app.route("/search/")
@app.route("/buscar/")
@app.route("/todos_los_Productos/")
@app.route("/all_product/")
def all_product():
    form = search()
    seh = form.seh
    return render_template('all_product.html', form=form, titulo='producto')

#Pagina de caro de compras
@app.route("/shopping_car/")
def shopping_car():
    return render_template('shopping_car.html', form=form, titulo='Carro de compras')

#Pagina de producto en especifico
@app.route("/producto/<string:name>/")
@app.route("/producto/")
def product(name="cafe del bueno"):
    form = comentar()
    coment = form.coment
    return render_template('product.html', form=form, titulo='producto')

#Pagina de dashboard platos
@app.route('/dashboard/')
@app.route('/dashboard/platos/')
def platos():
    form = search()
    return render_template('platos.html', form=form, titulo='dashboard')

#Pagina de dashboard gestion usuario
@app.route('/dashboard/usuarios/')
def usuarios():
    return render_template('usuarios.html', titulo='dashboard')

#Pagina agregar platos
@app.route('/dashboard/platos/add_plate/')
@app.route('/dashboard/platos/agregar_plato/')
def addPlatos():
    form = plate()

    return render_template('add_plate.html', form=form, titulo='dashboard')

#editar plato
@app.route('/dashboard/platos/edit_plate/')
@app.route('/dashboard/platos/editar_plato/')
def editPlato():
    form = plate()
    nPlato = form.nPlato
    pPlato = form.pPlato
    dPlato = form.dPlato
    aImgPlato = form.aImgPlato
    return render_template('edit_plate.html', form=form, titulo='dashboard')

#metodo para salir ;)
@app.route('/salir/')
def salir():
    session.clear()
    return render_template("index.html")


#ver perfil
@app.route('/perfil/')
@app.route('/profile/')
def verPerfil():
    form = profile()
    return render_template("profile.html", form=form)


#editar Perfil
@app.route('/perfil/editar_perfil/')
@app.route('/profile/edit_perfil/')
def editProfile():
    form = profile()
    return render_template("edit_profile.html", form=form)

#Cambiar contraseña
@app.route('/profile/change_password/')
@app.route('/perfil/cambiar_contraseña/')
def contraseña():
    form = password()
    return render_template("change_passsword.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

