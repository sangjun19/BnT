# dp를 사용해서 풀어야 함

result = 0

def dfs(y, x, n, arr, visited):
    global result    
    if y == len(arr) - 1 and x == len(arr[0]) - 1:
        if n == 0:
            result += 1
        return
    for dy, dx in [(1, 0), (0, 1)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr[0]):
            continue
        if arr[ny][nx] == 2:
            continue
        if (ny, nx) in visited:
            continue
        
        visited.append((ny, nx))
        if arr[ny][nx] == 1:
            dfs(ny, nx, n - 1, arr, visited)
        else:
            dfs(ny, nx, n, arr, visited)
        visited.pop()

def main():
    n, m, a, b = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(a):
        y, x = map(int, input().split())
        arr[y - 1][x - 1] = 1
    for _ in range(b):
        y, x = map(int, input().split())
        arr[y - 1][x - 1] = 2    
    dfs(0, 0, a, arr, [(0, 0)])
    print(result)
    
    
if __name__ == "__main__":
    main()