N = int(input())

lL = N % 10

if 10 < N < 20 or (lL != 1 and lL != 2 and lL != 3 and lL != 4):
    word = "korov"
elif lL == 1:
    word = "korova"
else:
    word = "korovy"

print(N, word)
