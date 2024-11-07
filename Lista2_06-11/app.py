from flask import Flask, render_template

app = Flask(__name__)

@app.route('/exercise1')
def form():
    return render_template('exercise1.html') 

@app.route('exercise4')
def automatico():
    return render_template('exercise4.html')


if __name__ == '__main__':
    app.run(debug=True)