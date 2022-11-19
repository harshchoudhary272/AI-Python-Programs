graph = {
    'H':['a','r'],
    'a':[],
    'r':['s'],
    's':['h'],
    'h':[]
}
visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)


#driver code
dfs(visited,graph,'H')

