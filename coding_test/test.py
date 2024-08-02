result = 0

def back(arr, cnt, sum, answer):
    global result
    if cnt == len(arr):
        if sum == answer:
            result += 1
        return
    for i in range(len(arr[cnt])):
        if sum + arr[cnt][i] <= answer:
            back(arr, cnt + 1, sum + arr[cnt][i], answer)

def main():
    n, m, k = map(int, input().split())
    arr = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        temp[0] = 0
        arr.append(temp)
    back(arr, 0, 0, k)
    print(result)

if __name__ == "__main__":
    main()