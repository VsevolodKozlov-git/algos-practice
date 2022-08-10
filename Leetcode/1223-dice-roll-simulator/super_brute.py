def brute():
    rollMax = [1,1,1,2,2,3]
    res = 0
    for i in range(6):
        for j in range(6):
            for k in range(6):
                rollMax[i] -= 1
                rollMax[j] -= 1
                rollMax[k] -= 1
                if rollMax[i] >= 0 and rollMax[j] >= 0 and rollMax[k] >= 0:
                    res += 1
                    print(i+1, j+1, k+1)
                rollMax[i] += 1
                rollMax[j] += 1
                rollMax[k] += 1
    return res

def forbiden():
    rollMax = [1,1,1,2,2,3]
    obey = 0
    for i in range(6):
        for j in range(6):
            for k in range(6):
                rollMax[i] -= 1
                rollMax[j] -= 1
                rollMax[k] -= 1
                if rollMax[i] < 0 or rollMax[j] < 0 or rollMax[k] < 0:
                    obey += 1
                rollMax[i] += 1
                rollMax[j] += 1
                rollMax[k] += 1
    return obey

if __name__ == '__main__':
    print(brute())