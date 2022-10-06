# your heading here

# Nicholas Tarsis, Jeff Chen, Vansh Saboo
# Running Hippos
# SoftDev
# k08 - serve
# 10-6-2022
# time spent:
# 0.7

from flask import Flask
import csv

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?


def hello_world():

    pass
#    print(__name__) # Q2: Where will this print to? Q3: What will it print?
#    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

#app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. Java :O
1. It looks like the root of a file system.
2. This will print to terminal.
3. It will print __main__, the file from which it was run.
4. This will appear on the webpage it makes. I know this because I downloaded Flask <3.
5. Java's driver files.
...

INVESTIGATIVE APPROACH:
We downloaded Flask. It gave us a link to the webpage it generated, and on it,
the returned String was on the webpage. print(__name__) printed "__main__" into
the terminal. We assume __name__ is the name of the current file it is running
from. Because app route is "/", we assume main is the default file.
'''
