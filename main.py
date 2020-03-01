#telegram @nickchuykov
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Chuykov Nick TI-82'

@app.route('/first')
def first():
    a = None
    b = 24
    c = 'Python is Cool!'
    return f'{a}, {b}, {c}'
    
@app.route('/second',methods = ["GET", "POST"])
def second():
    if  request.method == 'GET':
        return render_template('second.html')
    if request.method == 'POST':
        text = request.form.get('text')
        first = "".join(reversed(text))
        second = "".join([x for x in text[::-1]])
        third = text[::-1]
        return f'reversed: \t{first}<br/>comprehention: \t{second}<br/>slicing: \t{third}'


@app.route('/third',methods = ["GET", "POST"])
def third():
    pass

if __name__ == '__main__':
    app.run('0.0.0.0')