def main():
    n = int(input())
    arr = [1, 2, 5]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for a in arr:
            if i - a > 0:
                dp[i] += dp[i - a]
            if i - a == 0:
                dp[i] += 1
    print(dp[n])

if __name__ == "__main__":
    main()