#https://t.me/nickchuykov
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Chuykov Nikita TI-82'
@app.route('/first')
def variable_1():
    a,b,c = "kpi",None,1488
   
    return f'{a},{b},{c}'

@app.route('/second', methods=['GET', 'POST'])
def second():
    import pdb;
    pdb.set_trace()
    if request.method == 'GET':
        return render_template("Front.html")
    if request.method == 'POST':
        text = request.form['text']

        return str(text)







if __name__ == '__main__':
    app.run('0.0.0.0')
