t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    t -= 1
    string = ""
    for i in range(0,n,2):
        if (s[i:i+2]) == "00":
            string += "A"
        elif (s[i:i+2]) == "01":
            string += "T"
        elif (s[i:i+2]) == "10":
            string += "C"
        else:
            string += "G"
    print(string)
        
            
