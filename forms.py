from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, EqualTo


class Login(FlaskForm):
    usr = TextField('Usuario*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    pwd = PasswordField('Clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    btn = SubmitField('Ingresar')

class sign_in(FlaskForm):
    nom = TextField('Nombre*',validators=[Length(min=1, max=100, message='Longitud fuera de rango'),InputRequired(message='Nombre es requerido')])
    ema = EmailField('Email*',validators=[Length(min=3, max=100, message='Longitud fuera de rango'),InputRequired(message='Email es requerido')])
    usr = TextField('Usuario*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    cla = PasswordField('Clave*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    ver = PasswordField('Verificación*',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido'), EqualTo(cla, message='La clave y su verificación no corresponden')])
    btn = SubmitField('Registrar')