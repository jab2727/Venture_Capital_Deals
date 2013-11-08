import json
import networkx as nx

deal_list=json.load(open("investment_list.txt", "r"))

g=nx.Graph()

for company in deal_list:
	if company != "":
		g.add_node(company, type='company', Round=deal_list[company]['Series'], Size=deal_list[company]['Capital'])
		for investor in deal_list[company]['VC']:
			if investor != "":
				g.add_node(investor, type='investor')
				g.add_edge(company,investor)
		
print g.edges()

nx.write_graphml(g, "vc.graphml")
# Use graphML