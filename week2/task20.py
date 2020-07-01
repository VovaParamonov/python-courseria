a, b, c,  = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

result = "NO"

if a <= d:
    if b <= e or c <= e:
        result = "YES"
if b <= d:
    if a <= e or c <= e:
        result = "YES"
if c <= d:
    if a <= e or b <= e:
        result = "YES"

print(result)
