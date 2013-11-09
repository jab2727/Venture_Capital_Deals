import requests
import sys
import json

sitelist=[]

listfile = open("site_list.txt", "r")
for line in listfile:
	sitelist.append(line.strip())
listfile.close() 

def slice(text):	# looks at the first company's set of data
	text=str(text)
	switch=0

	if text.find("<p>")>=0 and (text.find("<p>") < text.find("<strong><br />") or text.find("<strong><br />") < 0):
		index1=text.index("<p>")
#		print "I found the first <p>"
	elif text.find("<strong><br />")>=0:		
		index1=text.index("<strong><br />")
#		print "I found the first <br /><strong><br /> at %s" % (index1)
	else:
#		print "I switched off immediately"
		switch=1
		
	if text.find("<strong><br />") == 0:
#		print "I've entered the loop..."
		n=2
		start=text.find("<strong><br />")
		while n >1:
			start=text.find("<strong><br />", start+len("<strong><br />"))
			n += -1			
		if  text.find("</p>")>0 and (text.find("</p>") < start or start<0):
			index2=text.index("</p>")+4
#			print "and I found a /p"
		else:
#			print "and I found a <br /><strong><br /> at %s" % (start)
			index2=start
	elif text.find("</p>") > 0 and text.find("<strong><br />") <0:
#		print "Skipped the loop and found a /p"
		index2=text.index("</p>")+4
	elif text.find("</p>") > 0 and text.find("<strong><br />") > text.find("</p>"):
#		print "Skipped the loop and found a /p"
		index2=text.index("</p>")+4
	elif text.find("<strong><br />")>0:
#		print "I skipped the loop and found a <br /><strong><br />"
		index2=text.index("<strong><br />")
	else:
#		print "I hit the second off switch"
		switch=1
	
	if switch==1:
		a=[]
	else:	
		a= text[index1:index2]
	return a

def dice(text):		# cuts the first company's data out of remaining data
	text=str(text)
	if text.find("<strong><br />") == 0:
		n=2
		start=text.find("<strong><br />")
		while n >1:
			start=text.find("<strong><br />", start+len("<strong><br />"))
			n += -1			
		if text.find("</p>")>0 and (text.find("</p>") < start or start<0):
			a=text[text.index("</p>")+4:len(text)]
		else:
			a=text[start:len(text)]
	elif text.find("</p>") > 0 and text.find("<strong><br />") <0:
		a=text[text.index("</p>")+4:len(text)]
	elif text.find("</p>") > 0 and text.find("<strong><br />") > text.find("</p>"):
		a=text[text.index("</p>")+4:len(text)]
	elif text.find("<strong><br />")>0:
		a=text[text.index("<strong><br />"):len(text)]
	else:
		a=[]
	return a
	
def get_name(text):	# finds the name of the company
	if text.find("<strong><br />")>=0 and text.find("<strong><br />")<10:
		name = text[text.index("<strong>")+14:text.index("</strong>")]
	elif text.find("<strong>")>=0 and text.find("<strong>")<10:
		name = text[text.index("<strong>")+8:text.index("</strong>")]
	elif text.find("<b>")>=0 and text.find("<b>")<10:
		name = text[text.index("<b>")+3:text.index("</b>")]
	else:
		name = "Name not found!"
	return name
	
def get_description(text):	# gets the text description of the company
	switch=0
	if text.find("</strong>")>0:
		index1=text.index("</strong>")+11
	elif text.find("</b>")>0:
		index1=text.index("</b>")+6
	else:
		switch=1	

	if text.find("raised")>0:
		index2=text.index("raised")-6
	elif text.find("secured")>0:
		index2=text.index("secured")-7
	else:
		switch=1
	
	if switch==1:
		description = "Description not found :/"
	else:
		description = text[index1:index2]
	return description
	
def get_capital(text):		# gets the value raised
	switch=0
	if text.find("raised")>0:
		index1=text.index("raised")+8
	elif text.find("secured")>0:
		index1=text.index("secured")+9
	else:
		switch=1
	
	if text.find("million")>0:
		index2=text.index("million")-1
	elif text.find("amount")>0:
		index2=text.index("amount")-1
	else:
		switch=1
	
	if switch==1:
		capital="Capital not found :/"
	else:
		try:
			return float(text[index1:index2])
		except:
			return ""
	
def get_series(text):	# gets the series round
	if text.find("million")>0:
		words = text[text.index("million"):text.index("million")+35]
	elif text.find("amount")>0:
		words = text[text.index("amount"):text.index("amount")+35]
	else:
		words=""
	if words.find("Series")>0 and words.find("Series")<25:
		return words[words.index("Series")+7]
	else:
		return "Series not specified"

def get_vc(text):
	if text.find("funding")>0:
		index1=text.index("funding")
	elif text.find("backers")>0:
		index1 = text.index("backers")
	elif text.find("Backers")>0:
		index1 = text.index("Backers")
	else:
		index1=0
		
	if text.find("href")>0:
		index2=text.index("href")
	elif text.find("</p>")>0:
		index2=text.index("</p>")
	else:
		index2=0
 	
 	passage = text[index1:index2]
	passage = passage.replace("<strong>"," ").replace("</strong>","").replace(">","").replace("<"," ")
	passage = passage.replace("\xc2\xa0"," ").replace("\xc3\xa9","e").replace("."," ").replace(" return",",").replace("\x82\xac","")
	passage = passage.split(", ")

	frag_list=[]
	name_list=[]

	for i in passage:
		fragment = str(i).split(" and ")
		for line in fragment:
			frag_list.append(line)

	flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

	for i in frag_list:
		words = str(i).split()
		names=str()
		for word in words:
			if word[0].isupper()==True or word[0].isdigit()==True:
				names+=word+" "
		name_list.append(names)
	return name_list

deal_list={}


for i in range(len(sitelist)):
	print sitelist[i]
	content = requests.get(sitelist[i]).content
	key_passage = content[content.index("storytext"):content.index("jp-post-flair")]
	while key_passage.find("target")>0:
		snippet=slice(key_passage)
		deal_list[get_name(snippet)] = {'Description': get_description(snippet), 
		'Capital': get_capital(snippet), 'Series':get_series(snippet),'VC':get_vc(snippet)}
		key_passage=dice(key_passage)
		print
		print snippet
		print 
		print deal_list[get_name(snippet)]
		print
		print

print deal_list


json.dump(deal_list, open("investment_list.txt", "w"))