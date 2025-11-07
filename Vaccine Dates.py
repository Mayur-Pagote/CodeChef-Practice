# cook your dish here
for i in range(int(input())):
    x,y,z = map(int, input().split())
    
    if y <= x <= z:
        print("Take second dose now")
    
    elif y < z < x:
        print("Too Late")
    
    else:
        print("Too Early")
