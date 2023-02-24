from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect

import forms

app=Flask(__name__)
app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect()

@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST' and reg_alum.validate:
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template('Alumnos.html', form=reg_alum, mat=mat, nom=nom)

@app.route("/cookie",methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)
    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        succes_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_user',datos)
        flash(succes_message)
    response=make_response(render_template('cookie.html',form=reg_user))
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        with open('colores.txt', 'a') as f:
            f.write(request.form['color_esp'] + ',' + request.form['color_eng'] + '\n')
        

        color = request.form['color']
        translation = ''
        with open('colores.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if parts[0] == color:
                    translation = parts[1] if request.form['radio'] == 'eng' else parts[0]
                    break
        return render_template('colores.html', color=color, translation=translation)
    
    return render_template('colores.html')

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)