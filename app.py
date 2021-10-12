from flask import Flask, render_template, request, session, flash
from markupsafe import escape
from wtforms import form
from forms import Login, sign_in, search, comentar, plate
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Pagina de inicio
@app.route("/Principal/")
@app.route("/home/")
@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')

#Pagina de inicar sesion
@app.route('/Entrar/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', form=form, titulo='Ingresar')

#Pagina de registrarse
@app.route("/Registrarse/")
@app.route("/sign_in/")
def sign():
    form = sign_in()
    nom = form.nom;
    apl = form.apl;
    ema = form.ema;
    usr = form.usr;
    ads = form.ads;
    num = form.num;
    cla = form.cla;
    ver = form.ver;
    btn = form.btn;
    return render_template('sign_in.html', form=form, titulo='Registro')

#Pagina de usuario
@app.route("/usuario/")
@app.route("/username/")
def username():
    return render_template('usuarios.html', titulo='usuario')

#Pagina de favoritos
@app.route("/favoritos/")
@app.route("/favorites/")
def favorites():
    return 'favorites'

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
@app.route('/dashboar/add_plate/')
@app.route('/dashboar/agregar_platos/')
def addPlatos():
    form = plate()
    nPlato = form.nPlato;
    pPlato = form.pPlato;
    dPlato = form.dPlato;
    aImgPlato = form.aImgPlato;
    return render_template('add_plate.html', form=form, titulo='dashboard')

@app.route('/dashboar/edit_plate/')
@app.route('/dashboar/editar_platos/')
def editPlato():
    form = plate()
    nPlato = form.nPlato;
    pPlato = form.pPlato;
    dPlato = form.dPlato;
    aImgPlato = form.aImgPlato;
    return render_template('edit_plate.html', form=form, titulo='dashboard')


if __name__ == '__main__':
    app.run(debug=True)

