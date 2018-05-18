from collections import defaultdict
import sys

#function to find the distance between two points in a graph
#in this function we need the weights,therefore the dictionary of the graph has been predefined
#also, we have added the weights to the edges of the graph, so to account for path distance 

def short_path(graph,s,t,visited=[],distances={},previous={}):
    #Find the shortest path between start and end nodes in a graph
    if s==t:
        #array that keeps record of the path that is being updated 
        path=[]
        while t != None:
            path.append(t)
            t=previous.get(t,None)
            
        return distances[s], path[::-1]
    
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[s]=0
    
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[s]:
        if neighbor not in visited:
            n = distances.get(neighbor,sys.maxsize)
            td = distances[s] + graph[s][neighbor]
            if td< n:
                distances[neighbor] = td
                previous[neighbor]= s
                
    # updating the visited nodes 
    visited.append(s)
    # find next nearest unvisited node from the graph 
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # closest node --> s
    return short_path(graph,closestnode,t,visited,distances,previous)

if __name__ == "__main__":
    
    graph1 = {'A': {'C': 1},
            'B': {'C':  4},
            'C': {'D':3},
            'D': {'E': 3},
            'E': {'F': 2},
            'F': {}}
    
    sp = short_path(graph1,'A','D')
    #displays the path and the shortest distance from the source to destination in the graph 
    print(sp)

