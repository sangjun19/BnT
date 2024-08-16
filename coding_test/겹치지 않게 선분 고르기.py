def main():
    n = int(input())
    arr = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        arr.append((x1, x2))
    arr.sort(key=lambda x: x[1])    
    dp = [1] * n
    for i in range(1, n):
        cnt = 0
        for j in range(0, i):
            if arr[j][1] < arr[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
    
if __name__ == "__main__":
    main()