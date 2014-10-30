import csv
cr = csv.reader(open("perf_produit.csv","rb"))

j=1;
r=0;
ag=[];
li=[];


for row in cr:
	if row[0]=='date': #pour ne pas prendre la premiere ligne, il existe surement une meilleure methode...
		li=li
	else:
		x = float(row[2]) #convertir en float les chaines de caracteres (ici la marge)
		y = float(row[3]) #convertir en float les chaines de caracteres (ici le cout_achat)
		z = float(row[4]) #convertir en float les chaines de caracteres (ici le CA)
		a = float(row[5]) #convertir en float les chaines de caracteres (ici le cout_var)
		b = float(row[6]) #convertir en float les chaines de caracteres (ici l ebe)
		li.append([row[0],x,y,z,a,b]) #on recopie les colonnes qui nous interessent (ici date, marge, cout_achat, CA, cout_var, ebe)

ag.append(li[0]) #initialisation de la variable ag avec la premiere ligne de li

while (j<len(li)):
	if ag[r][0]==li[j][0]: #si la date est la meme
		ag[r][1]= ag[r][1]+li[j][1] #la nouvelle marge est egale a lancienne plus la nouvelle
		ag[r][2]= ag[r][2]+li[j][2] #idem cout_achat
		ag[r][3]= ag[r][3]+li[j][3] #idem CA
		ag[r][4]= ag[r][4]+li[j][4] #idem cout_var
		ag[r][5]= ag[r][5]+li[j][5] #idem ebe
		j=j+1 #nouvelle ligne de li
	else:
		r=r+1
		ag.append(li[j]) #si la date change, on recopie la ligne de li correspondante
		j=j+1 #nouvelle ligne de li

c = csv.writer(open("agregat_jour.csv", "wb"))
c.writerow(["Jour","Marge","cout_achat","CA","cout_var","ebe"])
for elt in ag:
	c.writerow(elt)
