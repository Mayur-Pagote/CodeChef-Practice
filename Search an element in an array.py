def check_it(search, lis):
    if search[1] not in lis:
        return "NO"
    return "YES"

search_input = list(map(int, input().split()))
list_input = list(map(int, input().split()))

result = check_it(search_input, list_input)

print(result)
