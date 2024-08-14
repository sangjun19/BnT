jump_cnt = float('inf')

def jump(arr, cnt, pos):
    global jump_cnt
    if pos == len(arr) - 1:
        jump_cnt = min(jump_cnt, cnt)
        return
    for i in range(1, arr[pos] + 1):
        if pos + i < len(arr):
            jump(arr, cnt + 1, pos + i)
    return

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    jump(arr, 0, 0)
    if jump_cnt == float('inf'):
        print(-1)
    else:
        print(jump_cnt)
    
if __name__ == "__main__":
    main()