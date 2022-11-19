# This class represent a graph 
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
# Best-first search
def best_first_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate cost to goal
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('Jaipur', 'Gurgaon', 111)
    graph.connect('Faridabad', 'Mumbai', 85)
    graph.connect('Gurgaon', 'Nagpur', 104)
    graph.connect('Gurgaon', 'Shimla', 140)
    graph.connect('Gurgaon', 'Delhi', 183)
    graph.connect('Mumbai', 'Nagpur', 230)
    graph.connect('Mumbai', 'Kolkata', 67)
    graph.connect('Kolkata', 'Banaras', 191)
    graph.connect('Kolkata', 'Shimla', 64)
    graph.connect('Nagpur', 'Delhi', 171)
    graph.connect('Nagpur', 'Chennai', 170)
    graph.connect('Nagpur', 'Pune', 220)
    graph.connect('Shimla', 'Delhi', 107)
    graph.connect('Banaras', 'Patna', 91)
    graph.connect('Banaras', 'Raipur', 85)
    graph.connect('Patna', 'Raipur', 120)
    graph.connect('Raipur', 'Bangalore', 184)
    graph.connect('Bangalore', 'Delhi', 55)
    graph.connect('Bangalore', 'Chennai', 115)
    graph.connect('Chennai', 'Delhi', 123)
    graph.connect('Chennai', 'Pune', 189)
    graph.connect('Chennai', 'Kanpur', 59)
    graph.connect('Kanpur', 'Dharamshala', 81)
    graph.connect('Pune', 'Lucknow', 102)
    graph.connect('Dharamshala', 'Lucknow', 126)
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Banaras'] = 204
    heuristics['Patna'] = 247
    heuristics['Jaipur'] = 215
    heuristics['Kolkata'] = 137
    heuristics['Lucknow'] = 318
    heuristics['Mumbai'] = 164
    heuristics['Chennai'] = 120
    heuristics['Bangalore'] = 47
    heuristics['Nagpur'] = 132
    heuristics['Pune'] = 257
    heuristics['Kanpur'] = 168
    heuristics['Shimla'] = 75
    heuristics['Dharamshala'] = 236
    heuristics['Gurgaon'] = 153
    heuristics['Raipur'] = 157
    heuristics['Delhi'] = 0
    # Run search algorithm
    path = best_first_search(graph, heuristics, 'Jaipur', 'Delhi')
    print(path)
    print()
# Tell python to run main method
if __name__ == "__main__": main()
