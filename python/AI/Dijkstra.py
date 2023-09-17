class Graph:
    NODES = []
    EDGES = {}
    
    def add_node(self, name):
        self.NODES.append(name)
        self.EDGES[name] = []
    
    def add_edge(self, node1, node2, weight):
        if node1 not in self.NODES or node2 not in self.NODES:
            return
        if node1 in self.EDGES[node2]:
            return
        self.EDGES[node1].append((node2, weight))
        self.EDGES[node2].append((node1, weight))

G = Graph()

n = int(input("Enter the number of nodes in the graph: "))

for i in range(n):
    node = input("Enter node: ")
    G.add_node(node)

n = int(input("Enter the number of edges in the graph: "))

for i in range(n):
    node1 = input("Enter first node: ")
    node2 = input("Enter second node: ")
    weight = int(input("Enter the weight of the edge"))
    G.add_edge(node1, node2, weight)

source = input("Enter source node: ")

distance = {}
parent = {}

for v in G.NODES:
    distance[v] = float('inf')
    parent[v] = None
distance[source] = 0

explored = []
remaining = G.NODES.copy()

while remaining!=[]:
    u = None
    d = float('inf')
    for i in remaining:
        if distance[i] < d:
            u = i
            d = distance[i]
    explored.append(u)
    remaining.remove(u)
    for v in G.EDGES[u]:
        if distance[v[0]] > (distance[u] + v[1]):
            distance[v[0]] = distance[u] + v[1]
            parent[v[0]] = u

print(distance,parent,sep = '\n')