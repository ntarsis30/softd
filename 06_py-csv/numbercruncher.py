'''
Flying Chihuahuas: Nicholas Tarsis, Kosta Dubovskiy
Soft Dev
#6
22-09-29
'''

'''
DISCO:

* 
QCC:

HOW THIS SCRIPT WORKS:

'''
import random
import fileinput
def read():
    curr = []
    for line in fileinput.input(files = "occupations.csv"):
        if "\"" in line:
            curr.append(line.strip().split("\"")[1:])
        else:
            curr.append(line.strip().split(","))
    return curr[:-1]
    
print(read())