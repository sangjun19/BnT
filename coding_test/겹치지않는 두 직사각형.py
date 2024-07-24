def rectangle(sy, sx, ey, ex, arr):
    sum = 0
    for i in range(sy, ey + 1):
        for j in range(sx, ex + 1):
            sum += arr[i][j]
    return sum

def pick_pos(n, m, ay, ax, by, bx, arr):
    value = float("-inf")
    for i in range(ay, ay + n):
        for j in range(ax, ax + m):
            if i >= n or j >= m:
                continue
            for k in range(by, by + n):
                for l in range(bx, bx + m):
                    if k >= n or l >= m:
                        continue
                    
                    if i >= by and j >= bx:
                        continue
                    
                    v1 = rectangle(ay, ax, i, j, arr)
                    v2 = rectangle(by, bx, k, l, arr)
                    if v1 + v2 == 14:
                        print("A", ay, ax, i, j, v1)
                        print("B", by, bx, k, l, v2)
                    value = max(value, v1 + v2)
    return value

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = float("-inf")
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(m):
                    if i == k and j == l:
                        continue
                    # print(i, j, k, l)
                    # if j >= l:
                    #     continue
                    #print(i, j, k, l)
                    sum = pick_pos(n, m, i, j, k, l, arr)
                    result = max(result, sum)

    print(result)

if __name__ == "__main__":
    main()