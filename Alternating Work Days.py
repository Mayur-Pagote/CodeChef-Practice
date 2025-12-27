# cook your dish here


for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    
    if c%a == 0 and d%b == 0 and abs(c//a - d//b) <= 1:
        print("YES")
    else:
        print("NO")
