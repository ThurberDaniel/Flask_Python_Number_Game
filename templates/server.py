from flask import Flask, session, render, render_template, request, redirect
app = Flask(_name_)

app.secret_key = "09h8rgtiywbecTHUNDERnihfgDANIELq7uyiwueb"


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
