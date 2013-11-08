
sitelist=[]

listfile = open("site_list.txt", "r")
for line in listfile:
	sitelist.append(line.strip())
listfile.close() 

recent_entry = sitelist[0]

for i,j in enumerate(recent_entry):
	if j == "/":
		slashes.append(i)

year=recent_entry[slashes[2]+1:slashes[3]]
import requests

month=recent_entry[slashes[3]+1:slashes[4]]
day=recent_entry[slashes[4]+1:slashes[5]]
article=recent_entry[slashes[5]+23:slashes[6]]


sitelist=[]									#This code iterates through your list
											#and pulls up each line as a website.
listfile = open("site_list.txt", "r")		#
for line in listfile:						#It prints the data out, but eventually
	sitelist.append(line.strip())			#that "print" can be replaced
listfile.close() 							#with the function that analyzes
											#the website you're looking at.
for i in range(len(sitelist)):				#Probably makes sense to make that a 
	print sitelist[i]						#function.
