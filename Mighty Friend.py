# cook your dish here
for i in range(int(input())):
    N, K = map(int, input().split())
    elements = list(map(int,input().split()))
    motu = []
    tomu = []
    for i in range(N):
        if i % 2 == 0:
            motu.append(elements[i])
        else:
            tomu.append(elements[i])
    
    for j in range(K):
        max_ele = max(motu)
        motu.remove(max_ele)
        min_ele = min(tomu)
        tomu.remove(min_ele)
        
        tomu.append(max_ele)
        motu.append(min_ele)
    
    if sum(tomu) > sum(motu):
        print("YES")
    else:
        print("NO")
        
