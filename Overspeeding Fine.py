# cook your dish here
for i in range(int(input())):
    user = int(input())
    if user <= 70:
        print(0)
    elif user > 70 and user <= 100:
        print(500)
    else:
        print(2000)
