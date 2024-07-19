n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(m - 2):
        temp = 0
        for k in range(3):
            temp += arr[i][j + k]
        result = max(result, temp)
for i in range(n - 2):
    for j in range(m):
        temp = 0
        for k in range(3):
            temp += arr[i + k][j]
        result = max(result, temp)

for i in range(n - 1):
    for j in range(m - 1):
        sum_arr = [0] * 4
        for k in range(2):
            for l in range(2):
                y, x = i + k, j + l
                if not(k == 0 and l == 0):
                    sum_arr[0] += arr[y][x]
                if not(k == 0 and l == 1):
                    sum_arr[1] += arr[y][x]
                if not(k == 1 and l == 0):
                    sum_arr[2] += arr[y][x]
                if not(k == 1 and l == 1):
                    sum_arr[3] += arr[y][x]
        result = max(result, *sum_arr)
print(result)