def rectangle(sy, sx, ey, ex, arr):
    sum = 0
    for i in range(sy, ey + 1):
        for j in range(sx, ex + 1):
            sum += arr[i][j]
    return sum

def pick_pos(n, m, ay, ax, by, bx, arr):
    value = 0
    for i in range(ay, ay + n - 1):
        for j in range(ax, ax + m - 1):
            if i >= n - 1 or j >= m - 1:
                continue
            if j >= bx:
                continue
            for k in range(by, by + n - 1):
                for l in range(bx, bx + m - 1):
                    if k >= n - 1 or l >= m - 1:
                        continue
                    v1 = rectangle(i, ay, j, ax, arr)
                    v2 = rectangle(k, bx, l, by, arr)
                    value = max(value, v1 + v2)
    return value

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        for j in range(m - 1):
            for k in range(i, n):
                for l in range(j + 1, m):
                    sum = pick_pos(n, m, i, j, k, l, arr)
                    result = max(result, sum)

    print(result)

if __name__ == "__main__":
    main()