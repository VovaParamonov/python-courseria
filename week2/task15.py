x = int(input())
y = int(input())

amountOfRooms = y - x + 1
if (x - 1) % amountOfRooms == 0:
    print("YES")
else:
    print("NO")
