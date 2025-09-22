# cook your dish here
w,x,y,z = map(int, input().split())

if (w*2 + x) == (y*2 + z):
    print("Equal")
elif (w*2 + x) > (y*2 + z):
    print("Messi")
else:
    print("Ronaldo")
