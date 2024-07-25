is_end = False
is_conflicted = False
time_count = 0
save_time = 0

class MinMax:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

class Marble:
    def __init__(self, x, y, weight, dir):
        self.x = x
        self.y = y
        self.weight = weight
        self.dir = dir

def is_conflict(marbleList, minmaxList):
    global is_conflicted, time_count, is_end, save_time
    global x_min, x_max, y_min, y_max
    new_marbleList = []
    out_count = 0
    flag = is_conflicted
    for i in range(len(marbleList)):
        if marbleList[i].x < minmaxList.min_x or marbleList[i].x > minmaxList.max_x or marbleList[i].y < minmaxList.min_y or marbleList[i].y > minmaxList.max_y:
            out_count += 1            
            continue
        
        for j in range(len(marbleList)):
            if i == j: continue
            # print(marbleList[i].x, marbleList[i].y, marbleList[j].x, marbleList[j].y)
            if marbleList[i].x == marbleList[j].x and marbleList[i].y == marbleList[j].y:
                # print(i, j)
                # print(marbleList[i].x, marbleList[i].y, marbleList[j].x, marbleList[j].y)
                flag = True
                save_time = time_count
                if marbleList[i].weight > marbleList[j].weight or (marbleList[i].weight == marbleList[j].weight and i > j):
                    marbleList[j].weight = 0
                else:
                    marbleList[i].weight = 0
    
    is_conflicted = flag
    if out_count == len(marbleList):
        is_end = True
    for marble in marbleList:
        if marble.weight != 0:
            new_marbleList.append(marble)
    return new_marbleList

def print_marble(marbleList):
    print()
    for marble in marbleList:
        print(marble.x, marble.y, marble.weight, marble.dir)
    print()
        
def move_marble(marbleList, minmaxList):
    global time_count, is_end, is_conflicted, save_time
    dir = [[0, 0.5], [-0.5, 0], [0, -0.5], [0.5, 0]]
    while not is_end:
        for marble in marbleList:
            marble.x += dir[marble.dir][0]
            marble.y += dir[marble.dir][1]
        time_count += 1
        marbleList = is_conflict(marbleList, minmaxList)
        
    if not is_conflicted: print(-1)
    else: print(save_time)
    return
    
def main():
    global is_end, time_count, is_conflicted, save_time
    global x_min, x_max, y_min, y_max
    testCase = int(input())
    marble_case = []
    minmax_case = []
    for _ in range(testCase):
        x_min, y_min = float("inf"), float("inf")
        x_max, y_max = float("-inf"), float("-inf")
        marbleNum = int(input())
        marbleList = []
        minmaxList = []
        for _ in range(marbleNum):
            marbleObj = list(input().split())
            if marbleObj[3] == 'U':
                d = 0
            elif marbleObj[3] == 'D':
                d = 2
            elif marbleObj[3] == 'L':
                d = 1
            elif marbleObj[3] == 'R':
                d = 3
            x_min = min(x_min, int(marbleObj[0]))
            x_max = max(x_max, int(marbleObj[0]))
            y_min = min(y_min, int(marbleObj[1]))
            y_max = max(y_max, int(marbleObj[1]))
            marbleList.append(Marble(float(marbleObj[0]), float(marbleObj[1]), int(marbleObj[2]), d))            
        minmax_case.append(MinMax(x_min, x_max, y_min, y_max))
        marble_case.append(marbleList)
        
        
    for t in range(testCase):
        is_end = False
        is_conflicted = False
        time_count = 0
        save_time = 0
        move_marble(marble_case[t], minmax_case[t])
        
    
if __name__ == "__main__":
    main()