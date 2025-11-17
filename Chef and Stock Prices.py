# cook your dish here
for i in range(int(input())):
    x,y,z,p = map(int, input().split())
    percent = p/100
    stock = x + (x*percent)
    if y <= stock <= z:
        print("Yes")
    else:
        print("No")
