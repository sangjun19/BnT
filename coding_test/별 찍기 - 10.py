def function(arr, limit):    
    if limit == 1:
        return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
        
    arr = [[' '] * limit for _ in range(limit)]
    
    for i in range(0, limit, limit // 3):
        for j in range(0, limit, limit // 3):
            if i // (limit // 3) == 1 and j // (limit // 3) == 1:
                continue
                        
            temp = function(arr, limit // 3)                        
            
            for k in range(limit // 3):
                for l in range(limit // 3):
                    arr[i + k][j + l] = temp[k][l]
    return arr

def main():
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    arr = function(arr, n)
    for a in arr:
        print("".join(a))

if __name__ == "__main__":
    main()