

while True:
    string = input()
    value = ord(string)
    
    if value >= ord('a') and value <= ord('z'):
        print(string)
    elif value >= ord('A') and value <= ord('Z'):
        print(string)
    elif value >= ord('0') and value <= ord('9'):
        print(value)
    else:
        break