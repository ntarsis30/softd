#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#K19 -- Login
#2022-11-03
#time spent: 1
from flask import Flask,session,request, redirect, url_for,render_template
import os 

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = os.urandom(32)

USER = "user"
PASS = "pass"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'username' in session:
            return render_template('response.html', response="You are logged in as " + session['username'])
        return render_template("login.html")
    username = request.form['username']
    password = request.form['password']
    if username != USER:
        return render_template('login.html', error='Bad username')
    if password != PASS:
        return render_template('login.html', error='Bad password')
    session['username'] = username
    return redirect(url_for('login')) 

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()