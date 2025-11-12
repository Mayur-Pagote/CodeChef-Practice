# cook your dish here
for i in range(int(input())):
    num = int(input())
    if 1 <= num < 100:
        print("Easy")
    elif 100 <= num < 200:
        print("Medium")
    else:
        print("Hard")
