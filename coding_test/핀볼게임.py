def move_ball(arr, y, x, d):
    t = 1
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    ref = [[3, 2, 1, 0], [1, 0, 3, 2]]
    ny, nx = y, x
    while True:
        if arr[ny][nx] != 0:
            d = ref[arr[ny][nx] -1][d]
            
        ny = ny + dir[d][0]
        nx = nx + dir[d][1]
        t += 1
        if ny < 0 or nx < 0 or ny >= len(arr) or nx >= len(arr):
            break
    
    return t

def pin_ball(arr):
    result = 0    
    for k in range(len(arr)):
        result = max(result, move_ball(arr, 0, k, 2))
        result = max(result, move_ball(arr, k, 0, 3))
        result = max(result, move_ball(arr, k, len(arr) - 1, 1))
        result = max(result, move_ball(arr, len(arr) - 1, k, 0))
    print(result)

def main():
    n = int(input())    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    pin_ball(arr)
    
if __name__ == "__main__":
    main()