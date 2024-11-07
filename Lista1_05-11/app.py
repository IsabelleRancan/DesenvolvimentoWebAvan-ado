from flask import Flask, render_template

app = Flask(__name__)

@app.route('/exercise1')
def move_image():
    return render_template('exercise1.html') 

@app.route('/exercise2')
def take_image():
    return render_template('exercise2.html')

@app.route('/exercise3')
def table():
    return render_template('exercise3.html')

if __name__ == '__main__':
    app.run(debug=True)