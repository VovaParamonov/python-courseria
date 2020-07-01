n = int(input())
maxLength = 0
studLength = 0
lastNumber = n

while n != 0:
    if n == lastNumber:
        studLength += 1
        if studLength > maxLength:
            maxLength = studLength
    else:
        lastNumber = n
        studLength = 1

    n = int(input())

print(maxLength)
