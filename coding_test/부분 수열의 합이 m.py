def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    for a in arr:
        for i in range(m, 0, -1):
            if i - a >= 0:
                dp[i] = min(dp[i - a] + 1, dp[i])
    print(dp)
    
if __name__ == "__main__":
    main()