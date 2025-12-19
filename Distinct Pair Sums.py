# cook your dish here

for i in range(int(input())):
    L,R = map(int, input().split())
    res = 2*(R-L)+1
    print(res)


# Second sol
# cook your dish here

for i in range(int(input())):
    x,y = map(int, input().split())
    count = 0
    if x == y:
        print(1)
    else:
        
        print((2*y+1) - (2*x))
