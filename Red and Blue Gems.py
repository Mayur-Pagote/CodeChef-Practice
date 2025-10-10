# cook your dish here
x,y,z,k = map(int, input().split())

if x*z > y*k:
    print(x*z)
else:
    print(y*k)
