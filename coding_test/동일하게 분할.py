# 1트(실패)

# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     ans = sum(arr)
#     arr.sort()
#     for i in range(n):
#         result = 0
#         for j in range(i, n):
#             result += arr[j]
#             if ans - result == result:
#                 print("Yes")
#                 exit()        
#     print("No")
    
    
# if __name__ == "__main__":
#     main()

# 2트

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_arr = sum(arr)
    if sum_arr % 2 == 1:
        print("No")
        exit()
    
    ans = sum_arr // 2
    dp = [False] * (ans + 1)
    dp[0] = True
        
    for a in arr:
        for i in range(ans, a - 1, -1):
            dp[i] = dp[i] or dp[i - a]
    
    print("Yes" if dp[ans] else "No")

if __name__ == "__main__":
    main()