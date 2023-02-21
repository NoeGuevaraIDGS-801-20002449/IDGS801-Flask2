from flask import Flask, render_template, request
from forms import FormC

app=Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def cajas():
    if request.method == 'GET':
        CajaFor = FormC()
        return render_template('cajas.html', form=CajaFor)
    else:
        CajaFor = FormC(request.form)
        return render_template('cajas.html', form=CajaFor)

@app.route('/resultado', methods=['POST'])
def resultado():
    CajaFor = FormC(request.form)
    val = [int(number) for number in CajaFor.tCaja.data]
    
    rep = []

    for valor in set(val):
        repeticiones = len([num for num in val if num == valor])
        if repeticiones > 1:
            rep.append((valor, repeticiones))

    return render_template('resultado.html', valores=val, minNum=min(val), maxNum=max(val), promedio=sum(val) / len(val), repetidos=rep)

if __name__=="__main__":
    app.run(debug=True,port=3000)