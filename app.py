from flask import Flask, render_template, request, session, flash
from markupsafe import escape
from wtforms import form
from forms import Login, sign_in, search, comentar
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/Principal/")
@app.route("/home/")
@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Entrar/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', form=form)

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

@app.route("/usuario/")
@app.route("/username/")
def username():
    return 'username'

@app.route("/favoritos/")
@app.route("/favorites/")
def favorites():
    return 'favorites'

@app.route("/search/")
@app.route("/buscar/")
@app.route("/todos_los_Productos/")
@app.route("/all_product/")
def all_product():
    form = search()
    seh = form.seh
    return render_template('all_product.html', form=form, titulo='producto')

@app.route("/shopping_car/")
def shopping_car():
    return render_template('shopping_car.html', form=form, titulo='Carro de compras')

@app.route("/producto/<string:name>/")
@app.route("/producto/")
def product(name="cafe del bueno"):
    form = comentar()
    coment = form.coment
    return render_template('product.html', form=form, titulo='producto')

@app.route('/platos')
def platos():
    form = search()
    return render_template('platos.html', form=form)

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')


if __name__ == '__main__':
    app.run(debug=True)

