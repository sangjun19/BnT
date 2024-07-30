score = 0

def play_game(arr, end, player, move, limit):
    global score
    if limit == len(arr):
        count = 0
        # print(move)
        for i in range(len(move)):
            if move[i] >= end:
                count += 1
        score = max(score, count)
        return
    for i in range(player):
        move[i] += arr[limit]
        play_game(arr, end, player, move, limit + 1)
        move[i] -= arr[limit]

def main():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    play_game(arr, m, k, [1] * k, 0)
    print(score)
    
if __name__ == "__main__":
    main()