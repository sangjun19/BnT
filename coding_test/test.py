result = 0

def back(arr, k, sum, limit):
    global result
    if limit == 0:
        if sum == k:
            result += 1
    for i in range(len(arr)):
        if sum + arr[i] <= k:
            back(arr[i + 1:], k, sum + arr[i], limit - 1)
    
def main():
    global result
    n, k1, k2 = map(int, input().split())
    arr = list(map(int, input().split()))
    back(arr, k1, 0, 2)
    print(result, end=' ')
    
    result = 0
    back(arr, k2, 0, 2)
    print(result, end=' ')
    
if __name__ == "__main__":
    main()