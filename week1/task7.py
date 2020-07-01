N = int(input())

print((N - (N % 10) - (N // 100 * 100)) // 10)
