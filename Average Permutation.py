for i in range(int(input())):
    num = int(input())
    if num == 3:
        print("1 2 3")
    else:
        left = []
        right = []
        for j in range(1, num+1):
            if j % 2 != 0:
                left.append(str(j))
            else:
                right.append(str(j))
            
        left.reverse()
        res = left+right
        print(" ".join(res))
