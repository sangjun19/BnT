n = int(input())
arr = []
result = [[0] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
result[0][0] = arr[0][0]
for i in range(n):
    for j in range(n):
        if i != 0:
            result[i][j] = max(result[i][j], result[i - 1][j] + arr[i][j])
        if j != 0:
            result[i][j] = max(result[i][j], result[i][j - 1] + arr[i][j])
print(max(result[n - 1]))