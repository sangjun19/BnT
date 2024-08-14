def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = [[(0, 0)] * n for _ in range(n)]
    result[0][0] = (arr[0][0], arr[0][0])
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 and j == 0: continue
            
            minNum1, maxNum1 = (float('inf'), float('-inf'))
            minNum2, maxNum2 = (float('inf'), float('-inf'))
            dif1, dif2 = float('inf'), float('inf')
            
            if i != 0:
                minNum1, maxNum1 = result[i - 1][j]
                minNum1, maxNum1 = min(minNum1, arr[i][j]), max(maxNum1, arr[i][j])
                dif1 = maxNum1 - minNum1
            if j != 0: 
                minNum2, maxNum2 = result[i][j - 1]
                minNum2, maxNum2 = min(minNum2, arr[i][j]), max(maxNum2, arr[i][j])
                dif2 = maxNum2 - minNum2
            
            if dif1 < dif2:
                result[i][j] = (minNum1, maxNum1)
            else:
                result[i][j] = (minNum2, maxNum2)
                
            print(minNum1, maxNum1, minNum2, maxNum2)
                
            print()
            for r in result:
                print(*r)   
            
    minNum, maxNum = result[n - 1][n - 1]
    print(maxNum - minNum)
    
    
if __name__ == "__main__":
    main()