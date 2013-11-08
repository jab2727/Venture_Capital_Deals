import json
import networkx as nx

deal_list=json.load(open("investment_list.txt", "r"))
print deal_list['Onavo Mobile']['Series']