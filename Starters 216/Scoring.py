# cook your dish here
for i in range(int(input())):
    x,y = map(int, input().split())
    
    B = (y - x) // 2
    
    A = B + x
    
    print(A, B)
