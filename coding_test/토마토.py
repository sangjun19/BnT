from collections import deque

def main():
    m, n = map(int, input().split())    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    queue = deque()    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:                
                queue.append((i, j))
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m or arr[ny][nx] != 0:
                continue            
            
            arr[ny][nx] = arr[y][x] + 1
            queue.append((ny, nx))
    
    result = 0
    for a in arr:
        for t in a:
            if t == 0:
                print(-1)
                return
            result = max(result, t)
            
    print(result - 1)

if __name__ == "__main__":
    main()
