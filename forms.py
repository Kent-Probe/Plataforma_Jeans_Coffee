from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField, IntegerField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.widgets.core import TextArea

class Login(FlaskForm):
    name = TextField('Usuario*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    password = PasswordField('Clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    btn = SubmitField('Ingresar')

class sign_in(FlaskForm):
    nom = TextField('Nombres*',validators=[Length(min=5, max=50, message='Longitud fuera de rango'),InputRequired(message='Nombre es requerido')], )
    apl = TextField('Apellidos*',validators=[Length(min=5, max=50, message='Longitud fuera de rango')])

    ema = EmailField('Email*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='Email es requerido')])
    usr = TextField('Usuario*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    
    ads = TextField('Dirreccion*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='la direccion es requerido')])
    num = IntegerField('Numero*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='El numero telefonico es requerido')])
    
    
    cla = PasswordField('Clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    ver = PasswordField('Verificar clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido'), EqualTo(cla, message='Las claves no corresponden')])
    
    btn = SubmitField('Registrar')

class search(FlaskForm):
    seh = TextField('Buscar')

class comentar(FlaskForm):
    coment = TextAreaField('Comentario')

class plate(FlaskForm):
    pPlato = TextField('precio del plato')
    nPlato = TextField('Nombre del plato')
    dPlato = TextAreaField('Descripcion de plato')
    aImgPlato = TextAreaField('Agregar imagen')