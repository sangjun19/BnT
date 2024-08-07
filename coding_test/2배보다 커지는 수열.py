def main():
    def print_dp():
        for d in dp:
            for i in d:
                print(i, end=" ")
            print()    
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(1, m + 1):
        dp[1][j] = 1
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = sum(dp[i - 1][k] for k in range(1, j // 2 + 1)) % 1000000007
    # print_dp() 
    
    result = sum(dp[n][j]  for j in range(1, m + 1)) % 1000000007
    print(result)

if __name__ == "__main__":
    main()