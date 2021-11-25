from flask import Flask,request
from flask import render_template
from flask import url_for
from  werkzeug.security import generate_password_hash

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi hi'


@app.route('/prediction',methods=['POST', 'GET'])

def vue_form(name=None):
    error = None
    valeur=0
    name = request.form.get("name", "")
    age = request.form.get("age", "")
    response = "Hey there {}! You said you are {} years old.".format(name, age)

    if request.method == 'POST':
        if (request.form['username']):
            valeur=1
        else:
            error = 'Invalid username/password'

    return render_template("forlmulaire.html", error=error)

@app.route('/predit', methods=['POST', 'GET'])

def traitement():
    if request.method == 'POST':
        nom=request.form['nom']
        prenom=request.form['prenom']
        sexe=request.form['sexe']
        TDT=request.form['TDT']
        age=request.form['age']
        par=request.form['par']
        CHOL=request.form['CHOL']
        GAJ=request.form['GAJ']
        ECG=request.form['ECG']
        FCMAX=request.form['FCMAX']
        ANGINE=request.form['ANGINE']
        DEPRESSION=request.form['DEPRESSION']
        PENTE=request.form['PENTE']
        return "ça passe"
    else:
        return render_template("forlmulaire.html")


if __name__ == "__main__":
    app.run()
