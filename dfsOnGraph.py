
adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# adj_list = {
#     "A": ["B"],
#     "B": ["A", "D", "E"],
#     "C": ["F"],
#     "D": ["B"],
#     "E": ["B"],
#     "F": ["C"],
# }

color = {}  # White(unvisited) Grey(currently visiting) Black(fully visited)
parent = {}
trav_time = {}  # [start, end]
dfs_traversal_output = []

# initialization
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]
time = 0


def dfs(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1


for u in adj_list.keys():
    if color[u] == "W":
        dfs(u)

print("Output of traversed graph: ", dfs_traversal_output)
print("Parent of each node", parent)
print("Visit status: ", color)
print("Traversal time(Number of passes): ")
for node in adj_list.keys():
    print(node, " -> ", trav_time[node])
