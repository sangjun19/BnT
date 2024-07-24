def move(arr, r, c):
    print(arr[r][c], end=" ")
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for k in range(4):
        dy = r + dir[k][0]
        dx = c + dir[k][1]
        if dy < 0 or dx < 0 or dy >= len(arr) or dx >= len(arr):
            continue
        if arr[dy][dx] > arr[r][c]:
            return move(arr, dy, dx)
    return
        

def main():
    n, r, c = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    move(arr, r - 1, c - 1)

        
if __name__ == "__main__":
    main()