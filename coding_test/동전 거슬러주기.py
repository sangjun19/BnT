def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    for i in range(1, m + 1):
        for coin in arr:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    # print(dp)
    if dp[m] == float('inf'):
        print(-1)
        exit()
    print()
    
if __name__ == "__main__":
    main()