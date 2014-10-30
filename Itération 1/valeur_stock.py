# -*- coding: utf-8 -*-

import csv

cs=[element for element in csv.reader(open("suivi_stock.csv","rb"))]
vs = csv.writer(open("valeur_stock.csv", "wb"))
vs.writerow(["date","valeur_stock"])

li=[]
tab=[]
valeur=0
d=cs[1][0]

for i in range(1,len(cs)):
    if cs[i][0]==d:
        valeur=valeur+float(cs[i][2])*float(cs[i][3])
    else:
        li=[d,valeur]
        tab.append(li)
        d=cs[i][0]
        valeur=float(cs[i][2])*float(cs[i][3])
        if i==len(cs)-1:
            li=[d,valeur]
            tab.append(li)

for row in tab:
    vs.writerow(row)
        
