import copy

# 페어 개수 구하기
def calc_pair(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                continue
            if i != len(arr) - 1:
                if arr[i][j] == arr[i + 1][j]:
                    cnt += 1
            if j != len(arr) - 1:
                if arr[i][j] == arr[i][j + 1]:
                    cnt += 1
    return cnt

# 폭탄이 터진 후 내리기
def result_bomb(arr):    
    for j in range(len(arr)):
        save = -1
        for i in range(len(arr) - 1, -1, -1):
            if save == -1 and arr[i][j] == 0:
                save = i
            if arr[i][j] != 0 and save != -1:
                arr[save][j] = arr[i][j]
                arr[i][j] = 0
                save -= 1    
    return calc_pair(arr)

# 폭탄 터뜨리기
def bomb(arr, y, x): 
    dist = arr[y][x] - 1
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    arr[y][x] = 0
    for i in range(1, dist + 1):
        for k in range(4):            
            iy = y+ dir[k][0] * i
            ix = x + dir[k][1] * i
            if iy < 0 or ix < 0 or iy >= len(arr) or ix >= len(arr):
                continue
            arr[iy][ix] = 0    
    temp = copy.deepcopy(arr)
    return result_bomb(temp)

# 폭탄 고르기
def choose_bomb(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp = copy.deepcopy(arr)
            result = max(result, bomb(temp, i, j))
    return result

def print_arr(arr):
    print()
    for i in arr:
        for j in i:
            print(j, end=" ")        
        print()
    print()

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))    
    result = choose_bomb(arr[:])
    print(result)
    
if __name__ == "__main__":
    main()