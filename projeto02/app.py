from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'Hello World!'

@app.route('/contact')
def contact():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0")

