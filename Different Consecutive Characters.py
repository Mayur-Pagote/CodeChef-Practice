# cook your dish here

user = int(input())

for i in range(user):
    length = int(input())
    s = input()
    count = 0
    for i in range(length-1):
        if s[i] == s[i+1]:
            count += 1
    print(count)
