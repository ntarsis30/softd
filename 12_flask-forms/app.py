from flask import Flask, render_template, request 

app = Flask(__name__)   

@app.route("/")
def disp_loginpage():
    return render_template('login.html')

@app.route("/auth", methods=['GET', 'POST']) 
def authenticate():
    return render_template("response.html", username=request.form['username'], request=request.method)


if __name__ == "__main__": 
    app.debug = True        
    app.run()