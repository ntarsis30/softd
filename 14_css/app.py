# Flying Turtles: Nicholas Tarsis, Anson Wong
# SoftDev
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

app = Flask(__name__)    #create Flask object

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()