import sys

def bfs(v, edges):
    # Creating adjacency list
    adj = [[] for _ in range(v)]
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    # BFS
    parent = [-1 for _ in range(v)] 
    depth = [-1 for _ in range(v)] 
    bridge = [[0 for _ in range(v)] for _ in range(v)] 

    s = 0
    q = [s]
    parent[s] = -2
    depth[s] = 0
    front = 0
    while front < len(q):
        curr = q[front]; front += 1
        for i in adj[curr]:
            if parent[i] == -1:
                parent[i] = curr
                depth[i] = depth[curr] + 1
                q.append(i)
                bridge[curr][i] = bridge[i][curr] = 1

    vis_edges = [[0 for _ in range(v)] for _ in range(v)]
    for a,b in edges:
        if a == b or bridge[a][b] or vis_edges[a][b]: 
            continue
        vis_edges[a][b] = vis_edges[b][a] = 1

        while a != b:
            if depth[a] > depth[b]:
                p = parent[a]
                if p < 0: break
                bridge[a][p] = bridge[p][a] = 0
                a = p
            elif depth[b] > depth[a]:
                p = parent[b]
                if p < 0: break
                bridge[b][p] = bridge[p][b] = 0
                b = p
            else:
                pa, pb = parent[a], parent[b]
                if pa >= 0:
                    bridge[a][pa] = bridge[pa][a] = 0
                    a = pa
                if pb >= 0:
                    bridge[b][pb] = bridge[pb][b] = 0
                    b = pb
                if pa < 0 and pb < 0: 
                    break

    # Bridge elements
    bridge_store = []
    for i in edges:
        if bridge[i[0]][i[1]]:
            bridge_store.append((min(i[0], i[1]), max(i[0], i[1])))

    return bridge_store

file = sys.argv[1]

edges = []
with open(file,'r') as f:
  for line in f:
    edges.append([int(edge_str) for edge_str in line.split()])

# Number of nodes
v = 0
for i in edges:
  v = max(v,max(i[0],i[1]))
v += 1

# Printing the output
bridges = bfs(v, edges)
for i in bridges:
    print(i[0]," ",i[1])