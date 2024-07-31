bomb_cnt = 0
bomb_size = 0

def find_bomb(arr, y, x):
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    global bomb_cnt, bomb_size
    origin = arr[y][x]
    arr[y][x] = 0
    bomb_size += 1
    
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr) or arr[ny][nx] == 0 or arr[ny][nx] != origin:
            continue
        find_bomb(arr, ny, nx)            


def main():
    global bomb_size, bomb_cnt
    max_boom = 0
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            bomb_size = 0
            find_bomb(arr, i, j)
            if bomb_size >= 4:
                bomb_cnt += 1
            max_boom = max(max_boom, bomb_size)
    
    print(bomb_cnt, max_boom)

if __name__ == "__main__":
    main()