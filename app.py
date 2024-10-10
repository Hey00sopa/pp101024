from flask import Flask, render_template, request, redirect

app = Flask(__name__)

livros = []

@app.route('/')

def index():
    return render_template('index.html', livros = livros)

@app.route('/criar', methods=['POST'])
def create():
    nome = request.form['nome']
    livros.append(nome)
    return redirect('/')


@app.route('/alterar', methods=['POST']) #rota/ alterar
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    if old_name in livros:
        index = livros.index(old_name)
        livros[index] = new_name
    return redirect('/')


@app.route('/apagar', methods=['POST'])
def delete():
    nome = request.form['nome']
    if nome in livros:
        livros.remove(nome)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)

    