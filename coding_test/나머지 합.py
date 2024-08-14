# 1트 실패

# result = 0

# def back(arr, limit, m):
#     global result
#     if limit > len(arr):
#         return
    
#     if sum(arr[:limit]) % m == 0:
#         result += 1
        
#     back(arr, limit + 1, m)

# def main():
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for i in range(n):
#         back(arr[i:], 1, m)
#     print(result)
    
# if __name__ == "__main__":
#     main()

# 2트 dp 사용
# 두 누적합의 m으로 나눈 나머지가 같다면 두 누적합의 차이는 m의 배수이다.

def main():
    from collections import defaultdict
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix_sum = 0
    count = 0
    remainder_count = defaultdict(int)
    remainder_count[0] = 1
    
    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % m
        
        if remainder in remainder_count:
            count += remainder_count[remainder]
        
        remainder_count[remainder] += 1
        
    print(count)

if __name__ == "__main__":
    main()
