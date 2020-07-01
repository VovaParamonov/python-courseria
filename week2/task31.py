X = int(input())
maxVal = X
amountOfMax = 0

while X != 0:
    if X > maxVal:
        maxVal = X
        amountOfMax = 1
    elif X == maxVal:
        amountOfMax += 1
    X = int(input())

print(amountOfMax)
