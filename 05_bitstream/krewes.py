'''
WE KAN DOers: Nicholas Tarsis, Kosta Dubovskiy
Soft Dev
#5
22-09-28
'''

'''
DISCO:
Nicholas learned about randchoice
Konstantin learned about randrange
We reviewed file io with sys.stdin
We implemented f strings in our output
* 
QCC:
OPS SUMMARY:
'''
import random
import sys
sys.stdin = open("krewes.txt","r")

def read():
    s = input().split("@@@")[:-1]
    people_list = {}
    for i in s:
        stuff = i.split("$$$")
        if stuff[0] not in people_list:
            people_list[stuff[0]]=[]
        people_list[stuff[0]].append((stuff[1],stuff[2]))
    return people_list
        
    
    

def get_devo(krewes):
    rand_key = random.choice(list(krewes.keys()))
    rand_devo = krewes[rand_key][random.randrange(len(krewes[rand_key]))]
    return f'{rand_key}: ({rand_devo[0]}, {rand_devo[1]})'

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

print(get_devo(read()))
