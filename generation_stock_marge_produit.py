# -*- coding: utf-8 -*-

import csv
import datetime
cr = [element for element in csv.reader(open("WalletTransactions.csv","rb"))]
cs = csv.reader(open("stock_initial.csv","rb"))

stock = csv.writer(open("suivi_stock.csv", "wb"))
stock.writerow(["date","type","quantity","price","date_buy"])

marge_produit = csv.writer(open("marge_produit.csv", "wb"))
marge_produit.writerow(["date","type","marge"])

li=[]
tab=[]
temp=[]
d=''
q=0

marge=0
margetab=[]
bolean=0

# **** stock initial
for row in cs:
	li=[]
	if row[0]!='date':
		dat = datetime.datetime.strptime(row[0],'%d/%m/%Y').strftime('%Y-%m-%d')
		li.append(dat)
		for i in range(1,len(row)):
			li.append(row[i])
		li.append(dat)
		tab.append(li)

for row in tab:
	stock.writerow(row)

for t in range(70):
	# **** stock à temps j+1
	# reprend le stock de la veille
	for row in tab:
		dateobj = datetime.datetime.strptime(row[0],'%Y-%m-%d')
		d=(dateobj + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
		row[0]=d
	
	# ajoute le stock acheté à j+1 	
	for row in cr:
		li=[]
		if row[0]!='date':
			if row[7]=='Buy' and row[0].split(" ")[0]==d:
				li=[d,row[3],row[2],row[4],d]
				tab.append(li)
			
	# retire le stock vendu à j+1
			if row[7]=='Sell' and row[0].split(" ")[0]==d:
				q=0
				for rowtab in tab:
					bolean=0
					if rowtab[1]==row[3]:
						if q==0:
							q=int(rowtab[2]) - int(row[2])
							if q<0:		
								q=int(row[2]) - int(rowtab[2])
								rowtab[2]=0
								for rowmarge in margetab:
									if rowmarge[0]==d and rowmarge[1]==row[3]:
										rowmarge[2]=rowmarge[2]+(float(row[4]) - float(rowtab[3]))*(float(row[2])-float(q))
						  				bolean=1
						  		if bolean==0:
						  			marge=(float(row[4]) - float(rowtab[3]))*(float(row[2])-float(q))
						  			li=[d,row[3],marge]
						  			margetab.append(li)
							else:
								rowtab[2] = q
								for rowmarge in margetab:
									if rowmarge[0]==d and rowmarge[1]==row[3]:
										rowmarge[2]=rowmarge[2] + (float(row[4]) - float(rowtab[3]))*float(row[2])
										bolean=1
								if bolean==0:
									marge=(float(row[4]) - float(rowtab[3]))*float(row[2])
									li=[d,row[3],marge]
						  			margetab.append(li)
								break
						else:
							q=int(rowtab[2])-q
							if q<0:		
								q=-q
								for rowmarge in margetab:
									if rowmarge[0]==d and rowmarge[1]==row[3]:
									   rowmarge[2] = rowmarge[2] + (float(row[4]) - float(rowtab[3]))*float(rowtab[2])
								rowtab[2]=0
							else:
								for rowmarge in margetab:
									if rowmarge[0]==d and rowmarge[1]==row[3]:
									   rowmarge[2] = rowmarge[2] + (float(row[4]) - float(rowtab[3]))*float(int(rowtab[2])-q)
							 	rowtab[2]=q
								break
				if q<0:
					raise ValueError("erreur quantité de stock négative : " + row[3] )
	temp=[]
	for i in range(len(tab)):
		if tab[i][2]!=0:
			temp.append(tab[i])
	tab = temp

	for row in tab:
		stock.writerow(row)

for row in margetab:
		marge_produit.writerow(row)		
print len(margetab) 
