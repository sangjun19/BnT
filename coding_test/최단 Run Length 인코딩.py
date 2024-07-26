def main():
    A = input()
    n = len(A)
    result = float("inf")
    for i in range(n):
        log = []
        cnt = 1
        for k in range(1, n):
            cur = (i + k) % n
            prev = (i + k - 1) % n
            if A[cur] == A[prev]:
                cnt += 1
            else:
                log.append(cnt)
                cnt = 1
        log.append(cnt)
        sum = len(log)        
        for c in log:
            sum += (len(str(c)))
        result = min(result, sum)
    print(result)
if __name__ == "__main__":
    main()