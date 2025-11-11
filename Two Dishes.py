# cook your dish here
for i in range(int(input())):
    N,A,B,C = map(int,input().split())
    count = min(A,B)
    B -= A
    count += min(B,C)
    if count >= N:
        print("YES")
    else:
        print("NO")
        
