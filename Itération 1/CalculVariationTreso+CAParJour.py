import csv
cr = csv.reader(open("WalletTransactions.csv","rb"))
i=1;
j=1;
r=0;
li=[];
ca=[];
for row in cr:

	if row[0]!="date":
		if row[7]=='Sell':
			x=float(row[2])*float(row[4])
			x1=float(row[2])*float(row[4])*95/100
			li.append([row[0],x,x1])
			i=i+1

		else :
			x=-float(row[2])*float(row[4])
			li.append([row[0],0,x])
			i=i+1


ca.append([li[0][0].split(" ")[0],li[0][1],li[0][2]])
print ca
print li[10]

while (j<len(li)):

	if ca[r][0].split(" ")[0]==li[j][0].split(" ")[0]:
		if float(li[j][1])>0:
			ca[r][1]=ca[r][1]+float(li[j][1])
			ca[r][2]=ca[r][2]+float(li[j][2])
			j=j+1
			
		else :
			ca[r][2]=ca[r][2]+float(li[j][2])
			j=j+1
			


	else :
		ca.append([li[j][0].split(" ")[0],li[j][1],li[j][2]])
		r=r+1
		j=j+1



print len(ca)

c = csv.writer(open("CA+VariationTreso.csv", "wb"))
c.writerow(["Jour","CA","VariationTreso"])
for elt in ca:
	c.writerow(elt)



