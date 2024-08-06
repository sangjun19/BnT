def main():
    n = int(input())
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] * 2
        if i % 2 == 0:
            arr[i] += 1
        else:
            arr[i] -= 1
    print(arr[n] % 10007)
    
if __name__ == "__main__":
    main()