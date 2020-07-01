A = int(input())
B = int(input())
N = int(input())

totalCent = A * N * 100 + B * N

print(totalCent // 100, totalCent % 100)
