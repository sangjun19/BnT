def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [float('-inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] == float('inf'):
                continue
            if arr[j] + j >= i:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    
if __name__ == "__main__":
    main()