num_max = float('-inf')

def calculate(arr, num_dic, num_list):
    i = 0
    for item in num_dic:    
        num_dic[item] = num_list[i]
        i += 1
    result = num_dic[arr[0]]
    i = 1
    while i < len(arr):
        sign = arr[i]
        i += 1
        if sign == '+':
            result += num_dic[arr[i]]
        elif sign == '-':
            result -= num_dic[arr[i]]
        elif sign == '*':
            result *= num_dic[arr[i]]
        i += 1
    return result

def find_max(arr, limit, num_dic, num_list):
    global num_max
    if limit == 0:        
        num_max = max(num_max, calculate(arr, num_dic, num_list))
        return
        
    for i in range(1, 5):
        num_list.append(i)
        find_max(arr, limit - 1, num_dic, num_list)
        num_list.pop()

def main():
    arr = input()
    num_dic = {}
    for a in arr:
        if a != '-' and a != '*' and a != '+':
            num_dic[a] = 0
    find_max(arr, len(num_dic), num_dic, [])
    print(num_max)
    
if __name__ == "__main__":
    main()