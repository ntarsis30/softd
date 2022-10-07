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
import random
#
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
#
@app.route("/") # Q1: What points of reference do you have for meaning of '/'?




def read():
    jobs = {}
    with open("./occupations.csv", 'r') as file:
        csvreader = csv.reader(file)
        line_count = 0
        for row in csvreader:
            if line_count != 0:
                jobs[row[0]] = float(row[1])
            line_count = line_count + 1
        del jobs["Total"]
    jobs["Other"]= 0.2
    return jobs

def weighted_select(d):
    rnum = random.random() * 100
    running_val_sum = 0
    line = 0
    for k in d:
        if line != 0:
            running_val_sum += d[k]
        if running_val_sum >= rnum:
            return k
        line += 1

# final test
def hello_world():
#    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return weighted_select(read())  # Q4: Will this appear anywhere? How u know?
app.run()  # Q5: Where have you seen similar constructs in other languages?
