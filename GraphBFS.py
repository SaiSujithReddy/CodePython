#https://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/

#Things learnt

# Difference between a graph and tree is:-
# graph is bidirectional whereas tree isn't
# Tree cannot have a cyclic node where as graph can have

#Why defaultdict ?
#https://shirishweb.wordpress.com/2017/05/06/python-defaultdict-versus-dict-get/


#   defaultdict(<class 'list'>)
# {1: [2, 3], 2: [4, 5], 3: [5], 4: [6], 5: [6]}

# Assumption in this problem nodes start from 0 and incrementally adds to 6, also last node is cyclic

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*len(self.graph)
        queue = [s]

        #queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

g = Graph()

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(4,6)
g.addEdge(5,6)
g.addEdge(6,6)

g.BFS(0)