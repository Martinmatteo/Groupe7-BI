import csv
cr = csv.reader(open("WalletTransactions.csv","rb"))
i=1;
j=1;
r=0;
li=[];
ca=[];
for row in cr:

	if row[7]=='Sell':
		x=float(row[2])*float(row[4])
		li.append([row[0],x])
		i=i+1

ca.append([li[0][0].split(" ")[0],li[0][1]])
while (j<len(li)):
	if ca[r][0].split(" ")[0]==li[j][0].split(" ")[0]:

		ca[r][1]=ca[r][1]+float(li[j][1])
		j=j+1

	else :
		ca.append([li[j].split(" ")[0],li[j][1]])
		r=r+1
		j=j+1


print len(ca)

c = csv.writer(open("CA.csv", "wb"))
c.writerow(["Jour","CA"])
for elt in ca:
	c.writerow(elt)



