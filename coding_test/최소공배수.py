def function(n, m):
    i = max(n, m)
    idx = 1
    while True:
        temp = i * idx
        if temp % n == 0 and temp % m == 0:
            return temp
        idx += 1
n, m = map(int, input().split())
print(function(n, m))