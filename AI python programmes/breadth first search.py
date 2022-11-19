graph = {
    'S':['A','B'],
    'A':['C','D'],
    'B':['G','H'],
    'C':['E','F'],
    'D':[],
    'E':['K'],
    'F':[],
    'G':['I'],
    'H':[],
    'I':[],
    'K':[]
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end=" ")

        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


#driver code
bfs(visited,graph,'S')
