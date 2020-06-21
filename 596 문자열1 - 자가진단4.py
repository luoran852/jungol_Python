a = input()

string, length = a.split(' ')
length = int(length)

if len(string) >= length:
    string = string[-length:]

print(string[::-1])

# if b >= 5:
#     print('test')
# else:
#     print('true')
