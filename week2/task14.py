A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

differenceX = A1 - B1
differenceY = A2 - B2
if differenceX < 0:
    differenceX = -differenceX
if differenceY < 0:
    differenceY = - differenceY

if differenceX <= 1 and differenceY <= 1:
    print("YES")
else:
    print("NO")
