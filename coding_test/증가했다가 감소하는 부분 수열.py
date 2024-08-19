def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[1] * n for _ in range(2)]    
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[0][i] = max(dp[0][i], dp[0][j] + 1)
            ii = n - i - 1
            jj = n - j - 1        
            if arr[jj] < arr[ii]:
                dp[1][ii] = max(dp[1][ii], dp[1][jj] + 1)
        
    for i in range(n):
        dp[0][i] += dp[1][i]
    print(max(dp[0]) - 1)          

if __name__ == "__main__":
    main()