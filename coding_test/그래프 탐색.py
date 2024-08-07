from collections import defaultdict
cnt = 0

def dfs(graph, visited, start):    
    global cnt
    visited.append(start)
    if start not in graph:
        return
    for v in graph[start]:
        if v not in visited:
            cnt += 1
            dfs(graph, visited, v)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list) # 빈 리스트를 기본값으로 설정
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    dfs(graph, [], 1)
    print(cnt)
    
if __name__ == "__main__":
    main()