def main():
    n, m, k = map(int, input().split())
    arr = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp[1:])
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        coins = arr[i - 1]
        
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
        
        for coin in coins:
            for j in range(k, coin - 1, -1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - coin]) % 10007
                
    for d in dp:
        print(d)
    print(dp[n][k])
    
if __name__ == "__main__":
    main()