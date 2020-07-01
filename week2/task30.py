n = int(input())

maxVal, preMaxVal = 0, 0

while n != 0:
    if n >= maxVal:
        # maxVal, preMaxVal = n, maxVal
        preMaxVal = maxVal
        maxVal = n
    elif n >= preMaxVal:
        preMaxVal = n
    n = int(input())

print(preMaxVal)
