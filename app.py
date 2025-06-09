from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    numero = request.form['numero']
    return render_template('resultado.html', nome=nome, sobrenome=sobrenome, email=email, numero=numero)

if __name__ == '__main__':
    app.run(debug=True)
