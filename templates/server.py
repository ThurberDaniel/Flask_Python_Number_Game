from flask import Flask, session, render, render_template, request, redirect
app = Flask(_name_)

app.secret_key = "09h8rgtiywbecTHUNDERnihfgDANIELq7uyiwueb"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', ['POST'])
def guess():
    if 'random' not in session:
        session['random'] = random.randrange(1, 101)
    print '*** RANDOM GENERATED NUMBER ***', session['radnom']
    print request.form['guess']
    return redirect('/')


app.run(debug=True)
