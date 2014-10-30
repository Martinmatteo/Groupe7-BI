import csv
cr = csv.reader(open("WalletTransactions.csv","rb"))

i=1;
j=1;
r=0;
k=0;
li=[];
ca=[];
for row in cr:

	if row[7]=='Sell':
		x=float(row[2])*float(row[4])
		li.append([row[0].split(" ")[0],x,row[3]])
		i=i+1


ca.append(li[0])
k=0

while (j<len(li)):
	
	if ca[r][0]==li[j][0]:
		row=r
		while row < len(ca):
			if ca[row][2]==li[j][2]:
				ca[row][1]=ca[row][1]+li[j][1]
				row = len(ca)+5
				j=j+1


			else :
				row=row+1


		if row!=len(ca)+5:
			k=k+1
			ca.append(li[j])
			j=j+1


	else :
		r=k+1
		k=r
		ca.append(li[j])
		j=j+1


c = csv.writer(open("CAParJourParProduit.csv", "wb"))
c.writerow(["Jour","CA","Produit"])
for elt in ca:
	c.writerow(elt)
