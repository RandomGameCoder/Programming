class Graph:
    NODES = []
    EDGES = {}
    
    def add_node(self, name):
        self.NODES.append(name)
        self.EDGES[name] = []
    
    def add_edge(self, node1, node2):
        if node1 not in self.NODES or node2 not in self.NODES:
            return
        if node1 in self.EDGES[node2]:
            return
        self.EDGES[node1].append(node2)
        self.EDGES[node2].append(node1)

class Node:
    def __init__(self, name, parent):
        self.NAME = name
        self.PARENT = parent

def solution(node):
    l = [node.NAME]
    while node.PARENT != None:
        node = node.PARENT
        l.append(node.NAME)
    l = l[::-1]
    return l
        

def DFS(start, end):
    node = Node(start, None)
    if node.NAME == end:
        return solution(node)
    frontier = [node]
    explored = []
    while frontier!=[]:
        node = frontier.pop()
        explored.append(node.NAME)
        for i in G.EDGES[node.NAME]:
            child = Node(i, node)
            for j in frontier:
                if child.NAME == j.NAME:
                    break
            else:
                if child.NAME not in explored:
                    if child.NAME == end:
                        return solution(child)
                    frontier.append(child)
    return None

G = Graph()

n = int(input("Enter the number of nodes in the graph: "))

for i in range(n):
    node = input("Enter node: ")
    G.add_node(node)

n = int(input("Enter the number of edges in the graph: "))

for i in range(n):
    node1 = input("Enter first node: ")
    node2 = input("Enter second node: ")
    G.add_edge(node1, node2)

start = input("Enter the start node: ")
end = input("Enter the end node")

print(DFS(start, end))