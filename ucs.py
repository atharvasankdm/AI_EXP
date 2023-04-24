from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
       

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def ucs(self,goal,start):
        
        answer = []

        for i in range(len(goal)):
            answer.append(10**8)

        # priority queue
        queue = []

        visited = {}

        queue.append([0,start])

        count = 0

        while(len(queue) > 0):
            queue = sorted(queue)
            p = queue[-1]
            print(p)
            del queue[-1]

            #yaha pe multiplied by -1 isliye kyuki neeche jo queue mai negatives insert kar rhe hai usko original mai wapis convert karne ke liye
            p[0]*= -1


            # multiplied by -1 karke jab sort karenge toh aage wale indexes par largest distances wale rahenge and queue[-1] pe leeast distance wale rahenge jo apneko consider karna hai

            if p[1] in goal:

                index = goal.index(p[1])

                if answer[index]== 10**8:
                    count+=1
                
                if answer[index]> p[0]:
                    answer[index] = p[0]

                del queue[-1]

                queue = sorted(queue)
                if count==len(goal):
                    return answer
            

            if p[1] not in visited:

                for i in range(len(self.graph[p[1]])):
                    queue.append( [(p[0] + cost[(p[1], self.graph[p[1]][i])])* -1, self.graph[p[1]][i]])                

            visited[p[1]] = 1

        return answer



g= Graph()
cost = {}
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(3,1)
g.addEdge(3,6)
g.addEdge(3,4)
g.addEdge(1,6)
g.addEdge(4,2)
g.addEdge(4,5)
g.addEdge(2,1)
g.addEdge(5,2)
g.addEdge(5,6)
g.addEdge(6,4)

# add the cost
cost[(0, 1)] = 2
cost[(0, 3)] = 5
cost[(1, 6)] = 1
cost[(3, 1)] = 5
cost[(3, 6)] = 6
cost[(3, 4)] = 2
cost[(2, 1)] = 4
cost[(4, 2)] = 4
cost[(4, 5)] = 3
cost[(5, 2)] = 6
cost[(5, 6)] = 3
cost[(6, 4)] = 7

# goal state
goal = []
 
    # set the goal
    # there can be multiple goal states
goal.append(6)

# get the answer
answer = g.ucs(goal, 0)
 
    # print the answer
print("Minimum cost from 0 to 6 is = ",answer[0])