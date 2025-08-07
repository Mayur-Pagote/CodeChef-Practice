# cook your dish here
user = int(input())

for i in range(user):
    s = ""
    x = input()
    y = input()
    
    for i in range(5):
        if x[i] == y[i]:
            s += "G"
        else:
            s += "B"
    print(s)
