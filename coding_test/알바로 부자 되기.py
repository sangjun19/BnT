def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    dp = [0] * n    
    dp[0] = arr[0][2]
    for i in range(1, n):
        dp[i] = arr[i][2]
        for j in range(0, i):
            if arr[j][1] < arr[i][0]:
                dp[i] = max(dp[i], dp[j] + arr[i][2])
    print(*dp)
    print(max(dp))
    
if __name__ == "__main__":
    main()