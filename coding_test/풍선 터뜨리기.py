n = int(input())
arr = list(map(int, input().split()))
num = [i for i in range(1, n + 1)]
idx = 0

for i in range(n):
    print(num[idx], end=" ")
    num.pop(idx)
    idx = (idx + arr[idx] + len(arr)) % len(arr)
    arr.pop(idx)
    