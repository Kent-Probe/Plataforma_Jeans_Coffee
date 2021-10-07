from flask import Flask, render_template, request, session, flash
from markupsafe import escape
from wtforms import form
from forms import Login, sign_in
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/home/")
@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    frm = Login()
    if request.method=='GET':
        return render_template('login.html', form=frm, titulo='Ingresar')
    else:
        # 1. Recuperar los datos del formulario y le aplico transformaciones
        usr = frm.usr.data.strip()
        pwd = frm.pwd.data.strip()
        # 2. Validar (Siempre es una buena práctica)
        sw = True
        if len(usr)<5 or len(usr)>40:
            flash("El nombre de usuario es requerido, longitud no valida [5-40]")
            sw = False
        if len(pwd)<5 or len(pwd)>40:
            flash("El password es requerido, longitud no valida [5-40]")
            sw = False
        # 3. Ejecutar la acción - Login imposturado (simular)
        if sw and usr=='pedro' and pwd=='pedro':
            session['usuario'] = usr
            session['clave'] = pwd
            return render_template("home.html")
        else:
            flash("Usuario o contraseña no validos")
            return render_template('login.html', form=frm, titulo='Ingresar')



@app.route("/sign_in/")
def sign():
    form = sign_in
    return render_template('sign_in.html', form=form, titulo='Registro')

@app.route("/username/")
def username():
    return 'username'

@app.route("/favorites/")
def favorites():
    return 'favorites'

if __name__ == '__main__':
    app.run(debug=True)

