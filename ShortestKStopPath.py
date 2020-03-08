#!/usr/bin/env python
# coding: utf-8

# In[14]:


import networkx as nx
###########################################QUESTION 2 PART(c)#######################################################
'''Chose this implementation, as this problem does not have the Overlapping Subproblems Property and therefore
did not require a dynamic programming solution. The solution requires an exhaustive search either way, therefore 
I chose to use a modified DFS to compute shortest kstop paths from source to target'''
class Graph:
    def __init__(self, graph):
        self.G = graph
        self.V = list(graph.nodes)
        self.pathlist = []    
        
    def DFS(self, s, t, k, visited, path):
        # Mark the current node as visited and store in path 
        visited[self.V.index(s)] = True
        path.append(s)

        #This condition will print lists up to k stops only. 
        if len(path) <= k:
            # If current vertex is same as destination, then append a path to pathlist. BREAK CONDITION
            if s == t and len(path) == k:
                #This line stores a deep copy of this path. This way we will not be have a list of empty lists
                #at the end of this function. 
                self.pathlist.append(path[:])
                #print(path)
               
            else: 
                # If current vertex is not destination 
                #Recur for all the vertices adjacent to this vertex 
                for i in self.G.neighbors(s):#G.neighbors(s): 
                    if visited[self.V.index(i)] == False:
                        self.DFS(i, t, k, visited, path)

        #Recursively remove current vertex from path[] and mark it as unvisited 
        path.pop()
        visited[self.V.index(s)] = False
        
        '''Note: I was having trouble saving a copy of my path at the right time (within the 2nd if statement) and 
        turns out list.append() only takes a shallow copy. Due to the fact that I was clearing my list recursively to record
        a new path, when I tried to append a given path to my list of paths and print that outside of my DFS function, it would 
        return a list of empty lists. I needed to append "path[:]" (deep copy) to my list of paths to ensure it would append the full path before 
        as soon as it was complete.'''
         
    def printAllPaths(self, G, s, t, k):
        # Mark all the vertices as not visited (used in DFS function)
        visited =[False]*len(self.V) 
        #Create an array to store weights of individual paths in our list of paths.
        weights = []
        # Create an array to store paths used in DFS function
        path = [] 
        # Call the recursive helper function to print all paths and store them in pathlist
        #k + 2 to account for "excluding the source and target" from prompt
        self.DFS(s, t, k + 2, visited, path)
        
        #Calculate weight of all paths and take the minimum
        self.findWeight(G)
        
        '''This helper function calls DFS first to generate a my list of k-stop paths (pathlist) and then findWeigt 
        to find the min weight path in pathlist.'''
        
    
    def findWeight(self, G):
        weights = []
        kstopsum = 0
        
        for p in self.pathlist:
            for i in range(len(p)):
                if i + 1 != len(p):
                    #i is the index in our path representing a single vertex
                    #p[i] is the actual string value of the vertex at index i. We need this to reference G correctly.
                    kstopsum += G[p[i]][p[i+1]]['weight']
                    
            weights.append(kstopsum)
            #Reset kstopsum to 0. Otherwise, we carry over the weight of one path produce the combined weight of every kstop path in graph
            kstopsum = 0
            
        '''find the index of our min weight in weights array. This will be the corresponding index of our path in the 
        pathlist array, so print pathlist[index of the min weight] and we will get the shortest path'''
        
        #If weights is empty then our pathlist is empty and a kstop path doesnt exist
        if not weights:
            print('No such k-stop path exists. Perhaps try to change your k value. \n')
        #if only one kstoppath exists, print the first element of both lists
        elif len(weights) == 1:
            print(weights[0])
            print(self.pathlist[0])
        else:
            min_weight_path = int(min(weights))
            #print(self.pathlist[weights.index(min_weight_path)])
            print(f" Weight of minimum path: {min_weight_path} \n Path: {self.pathlist[weights.index(min_weight_path)]} \n")
    
        
        '''The outer loop in this function iterates through the elements (p represents a kstop path) in pathlist, 
        and the inner loop iterates through the elements of each kstop path in pathlist to generate a total weight.
        This total weight is appended to a weights array that will store the weight of each k-stop path (in the same order
        as our pathlists array) so the index of that weight will correspond to the index of the path is belongs to.'''
###########################################QUESTION 2 PART(c)#######################################################
###########################################STARTER CODE: QUESTION 2 PART(c)##########################################
def test1():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'V', length=40, weight=2.0)
    G.add_edge('EC', 'HUMN', length=40, weight=4.0)
    G.add_edge('V', 'HUMN', length=40, weight=1.0)

    return G

def test2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=3.0)
    G.add_edge('EC', 'B', length=40, weight=2.0)
    G.add_edge('A', 'C', length=40, weight=4.0)
    G.add_edge('A', 'D', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)
    G.add_edge('B', 'D', length=40, weight=3.0)
    G.add_edge('C', 'HUMN', length=40, weight=2.0)
    G.add_edge('D', 'HUMN', length=40, weight=3.0)
    G.add_edge('D', 'E', length=40, weight=3.0)
    G.add_edge('HUMN', 'F', length=40, weight=1.0)
    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    return G

def Question2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)

    return G


"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: None (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    pylab.title("Input Graph")
    pylab.show()
    
def main():
    ################## READ CAREFULLY ##############################
    
    ########QUESTION 2########
    # Note that you cannot use any networkx functionality
    # which makes the solution trivial
    #G = Question2()
    #G = test1()
    G = test2()
    draw_graph(G)
    Graph1 = Graph(G)
    # Call your function here that takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)

    #This specific networkx graph works for 2 < k < 8 becuase that is range of kstop paths from source to target
    Graph1.printAllPaths(G, 'EC', 'HUMN', 3)
    
if __name__ == "__main__":
    # The driver function
    main()


# In[ ]:




