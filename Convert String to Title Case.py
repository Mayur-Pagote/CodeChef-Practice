# cook your dish here
user = int(input())

for i in range(user):
    s = input()
    l = s.split()
    for i in range(len(l)):
        if l[i][0].isupper():
            continue
        else:
            l[i] = l[i].capitalize()
    print(" ".join(l))
