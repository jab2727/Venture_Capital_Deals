import json
import networkx as nx

deal_list=json.load(open("investment_list.txt", "r"))

g1=nx.Graph()
g2=nx.Graph()
g3=nx.Graph()

for company in deal_list:
	if company != "":
		size=deal_list[company]['Capital']
		if isinstance(size, float)==True:
			size=float(size)
		else:
			size=0.0
		g1.add_node(company.replace("\n",""), type='company', Round=deal_list[company]['Series'], Size=size,Description=deal_list[company]['Description'])
		for investor in deal_list[company]['VC']:
			if investor != "":
				g1.add_node(investor.replace("\n",""), type='investor')
				g1.add_edge(company.replace("\n",""),investor.replace("\n",""))

#print g1.edges()
nx.write_graphml(g1, "vcd.graphml")

#for edge in g1.edges:
#	print edge
for company in deal_list:
	if company != "":
#		print len(g1.neighbors(company))
#		print g1.neighbors(company)
		last_vc=""
		for vc in g1.neighbors(company.replace("\n","")):
			g2.add_node(vc.replace("\n",""))
			if last_vc !="":
				g2.add_edge(vc.replace("\n",""),last_vc)
			last_vc=vc.replace("\n","")

nx.write_graphml(g2, "vcs.graphml")
# &#10;