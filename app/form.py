from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    # Campo de texto obligatorio para el email del usuario, con validacion formato email
    email = StringField("Correo electrónico", validators=[DataRequired(), Email()])

    # Campo de contraseñaobligatorio con longitud minima de 6 caracteres
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])

    # Boton de envio del formulario
    submit = SubmitField("Iniciar sesión")
