# 시간초과 pypy3로 제출

def is_valid(sudo, cy, cx, num):
    
    for i in range(9):
        if sudo[cy][i] == num:
            return False
    
    for i in range(9):
        if sudo[i][cx] == num:
            return False
    
    y = (cy // 3) * 3
    x = (cx // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudo[y + i][x + j] == num:
                return False
    return True

def backtrack(sudo, empty, idx):
    if idx == len(empty):
        for s in sudo:
            print(*s)
        exit()
    
    y, x = empty[idx]
    for num in range(1, 10):
        if is_valid(sudo, y, x, num):
            sudo[y][x] = num
            backtrack(sudo, empty, idx + 1)                
            sudo[y][x] = 0
    
    return False

def main():
    sudo = []
    empty = []
    for _ in range(9):
        sudo.append(list(map(int, input().split())))
    
    for i in range(9):
        for j in range(9):
            if sudo[i][j] == 0:
                empty.append((i, j))
    
    backtrack(sudo, empty, 0)

if __name__ == "__main__":
    main()
