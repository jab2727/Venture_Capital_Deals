import requests
from datetime import date, timedelta

sitelist=[]

oldfile = open("site_list.txt", "r")
for line in oldfile:
	sitelist.append(line.strip())
oldfile.close() 

recent_entry = sitelist[0]

slashes=[]

for i,j in enumerate(recent_entry):
	if j == "/":
		slashes.append(i)

list_year=int(recent_entry[slashes[2]+1:slashes[3]])
list_month=int(recent_entry[slashes[3]+1:slashes[4]])
list_day=int(recent_entry[slashes[4]+1:slashes[5]])
article=int(recent_entry[slashes[5]+23:slashes[6]])+1

test_date=date(list_year, list_month, list_day)

while test_date != date.today():	
	testsite="http://finance.fortune.cnn.com/"+str(test_date.year)+"/"+str(test_date.month)+"/"+str(test_date.day)+"/venture-capital-deals-"+str(article)+"/"
	test_date += timedelta(days=1)
	print testsite
	if requests.get(testsite).status_code==200:
		article += 1
		sitelist.insert(0,testsite)
		

newfile = open("site_list.txt", "w")	# This adds the list items to a .txt
for item in sitelist:
	newfile.write(str(item)+"\n")
newfile.close()
