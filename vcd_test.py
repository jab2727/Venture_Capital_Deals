sitelist=[]

oldfile = open("site_list_backup.txt", "r")
for line in oldfile:
	sitelist.append(line.strip())
oldfile.close() 

recent_entry = sitelist[0]

slashes=[]

for i,j in enumerate(recent_entry):
	if j == "/":
		slashes.append(i)

year=recent_entry[slashes[2]+1:slashes[3]]
month=recent_entry[slashes[3]+1:slashes[4]]
day=recent_entry[slashes[4]+1:slashes[5]]
article=recent_entry[slashes[5]+23:slashes[6]]

print year
print month
print day
print article