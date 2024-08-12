def balloon_game(N, balloon_values):
    balloons = list(enumerate(balloon_values, start=1))  # (번호, 값) 쌍의 리스트
    result = []
    idx = 0  # 시작 인덱스

    while balloons:
        # 현재 풍선의 번호를 결과에 추가
        num, move = balloons.pop(idx)
        result.append(num)
        
        if not balloons:
            break
        
        # 다음 인덱스 계산
        if move > 0:
            idx = (idx + (move - 1)) % len(balloons)
        else:
            idx = (idx + move) % len(balloons)

    return result

# 입력 받기
N = int(input())
balloon_values = list(map(int, input().split()))

# 결과 출력
result = balloon_game(N, balloon_values)
print(" ".join(map(str, result)))
