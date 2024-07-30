result = float('inf')
result2 = float('-inf')

def calc_distance(y1, x1, y2, x2):
    return (y1 - y2)**2 + (x1 - x2)**2

def choose_far(arr, m, picked):
    global result2
    if m == 0:
        temp = calc_distance(picked[0][0], picked[0][1], picked[1][0], picked[1][1])
        print(temp)
        result2 = max(result2, temp)
        return
    for i in range(len(arr)):
        picked.append(arr[i])
        choose_far(arr[i + 1:], m - 1, picked)
        picked.pop()

def find_far(picked):
    global result2
    result2 = float('-inf')
    choose_far(picked, 2, [])
    return result2

def choose(arr, m, picked):
    global result
    if m == 0:
        result = min(result, find_far(picked))
        return
    for i in range(len(arr)):
        picked.append(arr[i])
        choose(arr[i + 1:], m - 1, picked)
        picked.pop()

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    choose(arr, m, [])
    print(result)
    
if __name__ == "__main__":
    main()