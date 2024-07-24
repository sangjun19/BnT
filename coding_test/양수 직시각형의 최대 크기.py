def calc(arr, i, iv, j, jv):
    sum = 0
    # print(i, iv, j, jv)
    for y in range(i, i + iv + 1):
        for x in range(j, j + jv + 1):
            if arr[y][x] > 0:
                sum += 1
            else: 
                return -1
    return sum

def find_rect(arr, i, j):
    result = -1
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if i + y >= len(arr) or j + x >= len(arr[0]):
                continue
            result = max(result, calc(arr, i, y, j, x))
            
    return result

def main():
    n, m = map(int, input().split())
    arr = []
    result = -1
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if arr[i][j] < 0:
                continue
            result = max(result, find_rect(arr, i, j))
    print(result)
    
if __name__ == "__main__":
    main()