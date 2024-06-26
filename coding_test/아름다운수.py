def is_beautiful_number(s):
    cnt = 0
    for i in range(0, len(s) - 1):
        cnt += 1
        if int(s[i]) == cnt:
            cnt = 0
            continue
        if s[i] != s[i + 1]:
            if int(s[i]) != cnt:
                return False
            else:
                cnt = 0

    if int(s[-1]) != cnt + 1:
        return False
    
    return True

def count_beautiful_numbers(n, current):
    if len(current) == n:
        if is_beautiful_number(current):
            return 1
        return 0
    
    total = 0
    for digit in range(1, 5):
        total += count_beautiful_numbers(n, current + str(digit))
    
    return total

def main():
    n = int(input().strip())
    result = count_beautiful_numbers(n, "")
    print(result)

if __name__ == "__main__":
    main()
