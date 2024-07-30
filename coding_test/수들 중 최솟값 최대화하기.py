result = float('-inf')

def find_min(arr, visited, limit):
    global result
    if limit == 0:
        min_num = float("inf")
        for i in range(len(visited)):
            min_num = min(min_num, arr[i][visited[i]])
        result = max(result, min_num)
    
    for i in range(len(arr)):
        if i not in visited:
            visited.append(i)
            find_min(arr, visited, limit - 1)
            visited.pop()                                    

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    find_min(arr, [], n)
    print(result)

if __name__ == "__main__":
    main()