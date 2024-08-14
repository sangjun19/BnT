# 탐색하야 할 것을 queue에 넣어놓고 시작, 각 시작 위치에서 탐색범위를 넓혀가며 탐색 가능
# deque를 사용, pop(0)을 사용하면 시간복잡도가 O(n)이 되지만, deque를 사용하면 O(1)이 된다.

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
