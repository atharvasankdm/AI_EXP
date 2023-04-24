from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self,u,v):
        self.graph[u].append(v)
        


    def BFS(self,s):
        
        queue = []
        queue.append(s)
        self.visited.append(s)

        while queue:
            s = queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(i)


    def DFS(self,s):
        
        print(s,end=" ")
        self.visited.append(s)

        for i in self.graph[s]:
            if i not in self.visited:
                self.DFS(i)


    def DLS(self,src,target,maxDepth):

        # self.visited.append(src)

        if src==target: return True

        if maxDepth<=0: return False

        for i in self.graph[src]:
            
            if self.DLS(i,target,maxDepth-1):
                return True
                
        return False
    


    def DFID(self,src,target,maxDepth):

        for i in range(maxDepth):
            if self.DLS(src,target,i):
                return True
            
        return False








g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

if g.DFID(0, 6, 2) == True:
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")

# while True:
    
    # x,y = input("Enter source and dest node").split()
    # x= int(x)
    # y= int(y)
    # g.addEdge(x,y)
    # stop = input("enter y if you have given all the information  else n")

    # if stop=="y":
    #     break
    
 


# print ("Following is Depth First Traversal"
#                   " (starting from vertex 0)")
# g.DFS(0)



