def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            for y in range(0, i):
                for x in range(0, j):
                    if dp[y][x] == 0:
                        continue
                    if arr[y][x] < arr[i][j]:
                        dp[i][j] = max(dp[i][j], dp[y][x] + 1)
    for d in dp:
        print(*d)
    print(max(map(max, dp)))
    
if __name__ == "__main__":
    main()