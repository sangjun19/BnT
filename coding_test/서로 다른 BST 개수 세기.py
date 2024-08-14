def main():
    n = int(input())
    arr = [1, 1]
    for i in range(2, n + 1):
        sum = 0
        for k in range(1, i + 1):
            sum += arr[k - 1] * arr[i - k]
        arr.append(sum)
    print(arr[n])

if __name__ == "__main__":
    main()