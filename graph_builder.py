import json
import networkx as nx

deal_list=json.load(open("investment_list.txt", "r"))

g1=nx.Graph()
g2=nx.Graph()
g3=nx.Graph()

for company in deal_list:
	if company != "":
		g1.add_node(company, type='company', Round=deal_list[company]['Series'], Size=deal_list[company]['Capital'], Description=deal_list[company]['Description'])
		for investor in deal_list[company]['VC']:
			if investor != "":
				g1.add_node(investor, type='investor')
				g1.add_edge(company,investor)

nx.write_graphml(g1, "vcd.graphml")

#for edge in g1.edges:
#	print edge
for company in deal_list:
	if company != "":
		print len(g1.neighbors(company))
#		print g1.neighbors(company)
		last_vc=""
		for vc in g1.neighbors(company):
			g2.add_node(vc)
			if last_vc !="":
				g2.add_edge(vc,last_vc)
			last_vc=vc

nx.write_graphml(g2, "vcs.graphml")
