def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    result = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(n):
            result[i + 1][j + 1] = arr[i][j]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1: continue
            result[i][j] = min(max(result[i][j], result[i - 1][j]), max(result[i][j], result[i][j - 1]))
    
    # for r in result:
    #     print(*r)
    print(result[n][n])
        
if __name__ == "__main__":
    main()