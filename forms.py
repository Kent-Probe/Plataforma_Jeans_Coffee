from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import IntegerField, PasswordField, SubmitField,TextAreaField, TextField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length
from wtforms.widgets.core import SubmitInput, TextArea


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
    aImgPlato = FileField('Imagen', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo se permiten imágenes')])
    
    btn = SubmitField('Agregar platos')
    btnE = SubmitField('Editar')

class profile(FlaskForm):
    nPorfile = TextField('Nombre ')
    aPellido = TextField('Apeliido')
    user = TextField('usuario')
    adress = TextField('direccion')
    ema = EmailField('Email',validators=[Length(min=5, max=40, message='Longitud fuera de rango')])
    verificarEma = EmailField('confirmar email',validators=[Length(min=5, max=40, message='Longitud fuera de rango'), EqualTo(ema, message='Los corre no corresponden')])
    num = IntegerField('Numero',validators=[Length(min=5, max=40, message='Longitud fuera de rango')])
    imgUser = TextAreaField('imagen')
    btn = SubmitField('Editar')

class password(FlaskForm):
    claV = PasswordField('Clave actual*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    cla = PasswordField('Clave nueva*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    ver = PasswordField('Verificar clave nueva*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido'), EqualTo(cla, message='Las claves no corresponden')])
    btn = SubmitField('Editar')

#class table(FlaskForm):
    