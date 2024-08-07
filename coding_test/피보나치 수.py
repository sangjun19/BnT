def fibo(n):
    sum = 0
    arr = [0, 1, 1]        
    for i in range(3, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]

def main():
    n = int(input())
    print(fibo(n))
    
if __name__ == "__main__":
    main()