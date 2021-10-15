from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, PasswordField, SubmitField,TextAreaField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length
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
    pPlato = TextField('precio del plato',validators=[InputRequired()])
    nPlato = TextField('Nombre del plato',validators=[InputRequired()])
    dPlato = TextAreaField('Descripcion de plato',validators=[InputRequired()])
    aImgPlato = FileField('Imagen', validators=[FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')])
    
    btn = SubmitField('Agregar platos')

class profile(FlaskForm):
    nPorfile = TextField('Nombre ',validators=[InputRequired()])
    aPellido = TextField('Apeliido',validators=[InputRequired()])
    user = TextField('usuario',validators=[InputRequired()])
    adress = TextField('direccion',validators=[InputRequired()])
    ema = EmailField('Email',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='Email es requerido')])
    verificarEma = EmailField('confirmar email',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='Email es requerido'), EqualTo(ema, message='Las claves no corresponden')])
    num = IntegerField('Numero',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), InputRequired(message='El numero telefonico es requerido')])
    imgUser = TextAreaField('imagen', validators=[InputRequired()])

class password(FlaskForm):
    cla = PasswordField('Clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    ver = PasswordField('Verificar clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido'), EqualTo(cla, message='Las claves no corresponden')])
