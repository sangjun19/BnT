class Marble:
    def __init__(self, x, y, weight, dir):
        self.x = x
        self.y = y
        self.weight = weight
        self.dir = dir
        
def check_conflict(marbleList, n):
    marble_map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(marbleList)):
        if marbleList[i].weight == 0: continue
        x, y = marbleList[i].x, marbleList[i].y
        
        if marble_map[x][y] != 0:
            marbleList[i].weight += marbleList[marble_map[x][y] - 1].weight        
            marbleList[marble_map[x][y] - 1].weight = 0
        marble_map[x][y] = i + 1
            
    return marbleList

def print_result(marbleList):
    max_weight = 0
    marble_count = 0
    for marble in marbleList:
        max_weight = max(max_weight, marble.weight)
        if marble.weight != 0:
            marble_count += 1
    print(marble_count, max_weight)
    

def move_marble(marbleList, n, time):
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for t in range(time):
        for marble in marbleList:
            x, y = marble.x, marble.y
            x += dir[marble.dir][0]
            y += dir[marble.dir][1]
            if x < 0 or x >= n or y < 0 or y >= n:
                marble.dir = (marble.dir + 2) % 4
                x += dir[marble.dir][0]
                y += dir[marble.dir][1]
            marble.x, marble.y = x, y
        marbleList = check_conflict(marbleList, n)
    print_result(marbleList)

def main():
    n, m, t = map(int, input().split())
    marbleList = []
    for _ in range(m):
        x, y, dir, weight = input().split()
        if dir == 'U': d = 0
        elif dir == 'D': d = 2
        elif dir == 'L': d = 1
        elif dir == 'R': d = 3
        marbleList.append(Marble(int(x) - 1, int(y) - 1, int(weight), d))
    move_marble(marbleList, n, t)
    
if __name__ == "__main__":
    main()