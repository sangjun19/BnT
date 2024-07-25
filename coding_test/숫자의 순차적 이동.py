def find_max(arr, num):
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != num:
                continue
            big = 0
            fy, fx = i, j
            for d in dir:
                ny = i + d[0]
                nx = j + d[1]
                if ny < 0 or nx < 0 or ny >= len(arr) or nx >= len(arr):
                    continue
                if big < arr[ny][nx]:
                    big = arr[ny][nx]
                    fy, fx = ny, nx
            arr[fy][fx] = arr[i][j]
            arr[i][j] = big
            return

def move_num(arr, t):
    for l in range(t):
        for k in range(len(arr) ** 2):
            find_max(arr, k + 1)
            # print()
    for a in arr:
        for b in a:
            print(b, end=" ")
        print()

def main():
    n, t = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    move_num(arr, t)

if __name__ == "__main__":
    main()