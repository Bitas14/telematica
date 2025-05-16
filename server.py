from flask import Flask, render_template
app = Flask(_name_)

@app.route('/')
def index():
    return 'Bienvenido al curso de Telemática'

@app.route('/render')
def render():
    return render_template('hello.html')

if _name_ == "_main_":
    app.run (host="0.0.0.0", port=8090)
