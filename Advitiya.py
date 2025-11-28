
user_input = int(input())
    
for i in range(user_input):
    ms = "ADVITIYA" 
    count = 0
    string = input().strip()
    for j in range (len(string)):
        count += (ord(ms[j]) - ord(string[j]) + 26) % 26
    print(count)
    
    
