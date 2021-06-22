from flask import Flask, session, render, render_template, request, redirect, random
app = Flask(_name_)

app.secret_key = "09h8rgtiywbecTHUNDERnihfgDANIELq7uyiwueb"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', ['POST'])
def guess():
    if 'random' not in session:
        session['random'] = random.randrange(1, 101)
    guess = request.form['guess']
    # print '*** RANDOM GENERATED NUMBER ***', session['radnom']
    # print request.form['guess']

    if guess < session['random']:
        session['guess'] = "low"
    elif guess > session['random']:
        session['guess'] = 'high'
    else
    session['guess'] = 'correct'

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
