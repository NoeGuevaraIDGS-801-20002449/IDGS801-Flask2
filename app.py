from flask import Flask, render_template
from flask import request

import forms

app=Flask(__name__)

@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST':
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template('Alumnos.html', form=reg_alum, mat=mat, nom=nom)


if __name__=="__main__":
    app.run(debug=True,port=3000)