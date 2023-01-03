import networkx as nx

g = nx.Graph()

g.add_edges_from([(1,3), (2,4), (1,2), (1,4)])

nx.draw(g, with_labels=True)