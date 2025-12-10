# cook your dish here
for i in range(int(input())):
    x,y = map(int, input().split())
    count = 0
    for j in range(1, x+1):
        if j > y:
            count += (j-y)
    print(count)
