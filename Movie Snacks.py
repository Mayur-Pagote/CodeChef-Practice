# cook your dish here
menu = list(map(int, input().split()))

if (menu[0] * 2 + menu[1] * 3 < menu[2] * 2 + menu[1]):
    print(menu[0] * 2 + menu[1] * 3)
else:
    print(menu[2] * 2 + menu[1] )
