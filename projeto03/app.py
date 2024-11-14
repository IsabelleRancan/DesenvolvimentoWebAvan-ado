from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def move_image():
    return render_template('index.html') 

@app.route('/message', methods = ['POST'])
def message():
    name = request.form.get('user')
    password = request.form.get('key')

    if not name or not password:
        return ("Dados incorretos")
    
    #return render_template('message.html')
    # Retornar os valores para verificar na página

    return f"Nome: {name}, Senha: {password}"


if __name__ == '__main__':
    app.run(debug=True)