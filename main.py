from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Chuykov Nikita TI-82'
@app.route('/first')
def variable_1():
    a = 'Kpi top'
    b = abc
    c = 123
    return f'a,b,c'

if __name__ == '__main__':
    app.run('0.0.0.0')
