import requests
from datetime import date, timedelta

sitelist=[]
test_date=date(2013,10,23)
article=422

while test_date.year > 2010 and article > 82:
	test_date += -timedelta(days=1)
	testsite="http://finance.fortune.cnn.com/"+str(test_date.year)+"/"+str(test_date.month)+"/"+str(test_date.day)+"/venture-capital-deals-"+str(article)+"/"
	code=requests.get(testsite).status_code
	if code==200:
		article += -1
		sitelist+=[testsite]
		print testsite

article=81
		
while test_date.year > 2010 and article > 0:
	test_date += -timedelta(days=1)
	testsite="http://finance.fortune.cnn.com/"+str(test_date.year)+"/"+str(test_date.month)+"/"+str(test_date.day)+"/venture-capital-deals-"+str(article)+"/"
	code=requests.get(testsite).status_code
	if code==200:
		article += -1
		sitelist+=[testsite]
		print testsite

file = open("sitel_list.txt", "w")	# This adds the list items to a .txt
for item in sitelist:
	file.write(str(item)+"\n")
file.close()
