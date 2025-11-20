for i in range(int(input())):
    U,V,A,S = map(int, input().split())
    if (U * U) - (2*A*S) <= (V * V):
        print("Yes")
    else:
        print("No")
