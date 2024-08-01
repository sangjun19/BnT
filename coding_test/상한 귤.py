def rotting(mandarin):
    def bfs():
        cnt.append(1)
        queue = []
        visited = []
        queue.append((i, j))
        result[i][j] = -1
        visited.append((i, j))
        while queue:
            y, x = queue.pop(0)
            value = cnt.pop(0)            
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                
                if ny < 0 or ny >= len(mandarin) or nx < 0 or nx >= len(mandarin):
                    continue
                if (ny, nx) in visited:
                    continue
                
                if value + 1 > result[ny][nx]:
                    continue
                
                if mandarin[ny][nx] == 1:                
                    result[ny][nx] = min(result[ny][nx], value)
                    visited.append((ny, nx))
                    queue.append((ny, nx))
                    cnt.append(value + 1)
    
    result = [[float('inf') for _ in range(len(mandarin))] for _ in range(len(mandarin))]
    for i in range(len(mandarin)):
        for j in range(len(mandarin)):
            if mandarin[i][j] == 2:
                cnt = []                
                bfs()

    for i in range(len(mandarin)):
        for j in range(len(mandarin)):
            if mandarin[i][j] == 1 and result[i][j] == float('inf'):
                result[i][j] = -2
            elif mandarin[i][j] == 0:
                result[i][j] = -1
            elif (mandarin[i][j] == 2 and result[i][j] == -1) or result[i][j] == float('inf'):
                result[i][j] = 0
    
    for r in result:
        for i in r:
            print(i, end=" ")
        print()

def main():
    n, k = map(int, input().split())
    mandarin = []
    for _ in range(n):
        mandarin.append(list(map(int, input().split())))
    rotting(mandarin)
    
if __name__ == "__main__":
    main()