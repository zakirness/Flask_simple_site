from flask import Flask, url_for, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Колледжа"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/gis')
def gis():
    return render_template('gis.html', title='Гис')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/success")
def success():
    user = "20-КИС-2"
    return user + "  Успешная авторизация!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')