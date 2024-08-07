def main():
    n, m, k = map(int, input().split())
    arr = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp[1:])
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # 사람 인원수 만큼
    for i in range(1, n + 1):
        coins = arr[i - 1]
        
        # 이전 사람의 경우의 수 복사(내가 선택하지 않았을 때)
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
        
        # 내가 선택할 수 있는 동전 순회
        for coin in coins:
            # 역방향 순회(중복 방지), 현재 선택한 동전을 제외한 이전 동전까지의 경우의 수를 더함
            for j in range(k, coin - 1, -1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - coin]) % 10007
                
    # for d in dp:
    #     print(d)
    print(dp[n][k])
    
if __name__ == "__main__":
    main()