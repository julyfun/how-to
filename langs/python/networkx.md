---
title: networkx
date: 2024-01-15 01:10:05
tags: []
---
this package works together with matplotlib.

```py
import networkx as nx
from matplotlib import pyplot as plt

g = nx.Graph()

g.add_node(1)

list(g.nodes())

g.add_nodes_from([3, 4])

print(g.nodes)

nx.draw(g)
nx.draw(g, with_labels=True)
plt.show()

g.add_node('coin')

g.add_edge(1, 2)
e = (2, 3)
g.add_edge(*e)

g.add_edges_from([(1, 3), (1, 4), (1, 5)])

G.remove_node(2)
G.remove_nodes_from([4, 5, H, 'coin'])
print("les sommets de G sont : ", G.nodes)

edgelist = [(0, 1), (1, 2), (2, 3)]
I = nx.Graph(edgelist)

edgelist1 = [(0, 1), (0, 2), (0, 3)]
edgelist2 = [(0, 4), (0, 5), (0, 6)]
G1 = nx.Graph(edgelist1)
G2 = nx.Graph(edgelist2)
H1 = nx.disjoint_union(G1, G2) # make two graph in the same one 
H2 = nx.compose(G1, G2) # make the same considering the node id

g = nx.petersen_graph() # a special graph

nx.draw_shell(g, nlist=[range(5, 10), range(5)]) # make 0, 1, 2, 3, 4 in a shell

options = {
    'node_color': 'yellow',
    'node_size': 500,
    'width': 2,
    'with_labels': True
}

nx.draw_random(G, **options)
plt.show()

nx.draw_circular(G, **options)
plt.show()

nx.draw_shell(G, nlist=[range(5, 10), range(5)], **options)
plt.show()

nx.draw(G)
plt.savefig("graph.png")

G2= nx.DiGraph () 
G2.add_edges_from([(0, 1),(1,0), (0, 2), (0, 3)])
nx.draw_random(G2, with_labels=True, font_weight='bold')
plt.show()
```

## draw in particular position

```py
G=nx.Graph()
G.add_edges_from([[1,2],[2,3],[3,1]])
position={1:[0,2],2:[2,0],3:[0,0]} #dictionnaire où on précise les coordonnées de chacun des sommets
nx.draw(G,pos=position)
```
