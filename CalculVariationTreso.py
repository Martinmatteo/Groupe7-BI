import csv
cr = csv.reader(open("WalletTransactions.csv","rb"))
i=1;
j=0;
r=0;
li=[];
var=[];
for row in cr:

	if row[0]!="date":
		if row[7]=='Sell':
			x=float(row[2])*float(row[4])*95/100 #vente
			li.append([row[0],x])
			i=i+1

		else :
			x=-float(row[2])*float(row[4])*105/100 #achat
			li.append([row[0],x])
			i=i+1

var.append([li[0][0].split(" ")[0],1000000000])

while (j<len(li)):

	if var[r][0].split(" ")[0]==li[j][0].split(" ")[0]:

		var[r][1]=var[r][1]+float(li[j][1])
		j=j+1

	else :
		var.append([li[j][0].split(" ")[0],var[r][1]+float(li[j][1])])
		r=r+1
		j=j+1

c = csv.writer(open("VariationTreso.csv", "wb"))
c.writerow(["Jour","VariationTreso"])
for elt in var:
	c.writerow(elt)



