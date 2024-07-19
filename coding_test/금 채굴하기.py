n, m = map(int, input().split())
arr = []
count = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    count += temp.count(1)
    arr.append(temp)

gold_cost = m * count
k = -1
result = 0
cost = 1
while cost <= gold_cost:
    k += 1
    cost = k * k + (k + 1) * (k + 1)
    for i in range(n):
        for j in range(n):
            sum = 0
            for y in range(-k, k + 1):
                for x in range(-k + abs(y), k - abs(y) + 1):
                    yy = i + y
                    xx = j + x
                    if 0 <= yy < n and 0 <= xx < n:
                        sum += arr[yy][xx]
            if sum * m >= cost:
                result = max(result, sum)
print(result)