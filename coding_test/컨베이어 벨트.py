def main():
    n, t = map(int, input().split())
    arr = []
    arr.append(list(map(int, input().split())))    
    arr.append(list(map(int, input().split())))    
    
    for k in range(t):
        temp0 = arr[0][n - 1]
        temp1 = arr[1][n - 1]
        for i in range(n - 1, 0, -1):
            arr[0][i] = arr[0][i - 1]
            arr[1][i] = arr[1][i - 1]        
        arr[0][0] = temp1
        arr[1][0] = temp0
    
    for value in arr:
        for i in value:
            print(i, end=" ")
        print()
    
if __name__ == "__main__":
    main()