max_city = 0
one_dim = []
bfs_visited = []

def bfs(graph, y, x, u, d):
    global bfs_visited    
    queue = []
    bfs_visited.append((y, x))
    queue.append((y, x))
    cnt = 0
    
    while queue:
        cnt += 1
        y, x = queue.pop(0)
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= len(graph) or nx < 0 or nx >= len(graph) or (ny, nx) in bfs_visited:
                continue
            diff = abs(graph[ny][nx] - graph[y][x])
            if diff < u or diff > d:
                continue
            bfs_visited.append((ny, nx))
            queue.append((ny, nx))
    
    return cnt

def choose(graph, cnt, visited, u, d, start):
    global max_city, bfs_visited
    if cnt == 0:
        bfs_visited = []
        city_cnt = 0        
        for y, x in visited:
            city_cnt += bfs(graph, y, x, u, d)
        max_city = max(max_city, city_cnt)
        return
    for i in range(start, len(one_dim)):
        visited.append(one_dim[i])
        choose(graph, cnt - 1, visited, u, d, i + 1)
        visited.pop()

def main():
    global one_dim
    n, k, u, d = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    one_dim = [(i, j) for i in range(n) for j in range(n)]    
    choose(graph, k, [], u, d, 0)
    print(max_city)
    
if __name__ == "__main__":
    main()