def re_build(arr, s, e):
    temp = []
    for i in range(len(arr)):
        if i >= s - 1 and i <= e - 1:
            continue
        temp.append(arr[i])
    return temp

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    s1, e1 = map(int, input().split())
    s2, e2 = map(int, input().split())
    arr = re_build(arr, s1, e1)
    arr = re_build(arr, s2, e2)
    print(len(arr))
    for a in arr:
        print(a)
    
if __name__ == "__main__":
    main()