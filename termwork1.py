from collections import defaultdict
class Graph:
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    def DFS(self, v):
 
        visited = set()
 
        self.DFSUtil(v, visited)
 

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

class Graph:
  
    def __init__(self,vertices):
  
        self.V = vertices
  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def DLS(self,src,target,maxDepth):
  
        if src == target : return True
  
        if maxDepth <= 0 : return False
  

        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False

    def IDDFS(self,src, target, maxDepth):

        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False
  
# Create a graph given in the above diagram
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
  
target = 6; maxDepth = 3; src = 0
  
if g.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")
    g.DFS(0)
    g.BFS(0)
