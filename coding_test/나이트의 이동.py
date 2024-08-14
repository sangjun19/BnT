from collections import deque

def bfs(arr, y, x):
    queue = deque()
    queue.append((y, x))    
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr) or arr[ny][nx] > 0:
                continue
            
            if arr[ny][nx] == -1:
                return arr[y][x]
            
            arr[ny][nx] = arr[y][x] + 1
            queue.append((ny, nx))
    return 0

def main():
    n = int(input())
    for _ in range(n):
        l = int(input())
        arr = [[0] * l for _ in range(l)]
        y, x = map(int, input().split())
        arr[y][x] = 1
        y2, x2 = map(int, input().split())
        arr[y2][x2] = -1
        if y == y2 and x == x2:
            print(0)
            continue
        print(bfs(arr, y, x))
    
if __name__ == "__main__":
    main()