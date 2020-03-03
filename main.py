# telegram @nickchuykov
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


@app.route('/second', methods=['GET', 'POST'])
def second():
    if request.method == 'GET':
        return render_template('/Front.html')
    if request.method == 'POST':
        text = request.form.get('text')
        rev1 = text[::-1]  # slice
        rev2 = "".join(list(reversed(text)))  # reversed
        rev3 = "".join([x for x in reversed(text)])  # comprehension
        return f'$lice: {rev1}</br>rever$ed: {rev2}</br>comprehen$ion: {rev3}</br>'


@app.route('/third', methods=["GET", "POST"])
def third():
    if request.method == 'GET':
        return render_template('/third.html', content='\u0020', deck=str(deck))
    else:
        if "shuffle" in request.form:
            deck.shuffle()
            value = "Deck was shuffled"
        elif "pop" in request.form:
            value = deck.pop()
        elif "get_random" in request.form:
            value = deck.get_random()
        else:
            num = request.form.get("index")
            value = deck.index(num)
        return render_template('third.html', content=value, deck=str(deck))  # printing the deck
        # you push buttons on this page again without reloading it


if __name__ == '__main__':
    app.run('0.0.0.0')
