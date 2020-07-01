A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())

equalStr = "Boxes are equal"
firstLargerStr = "The first box is larger than the second one"
secondLargerStr = "The first box is smaller than the second one"

result = "Boxes are incomparable"

# First Larger
if A1 <= A2:
    if (B1 <= B2 and C1 <= C2) or (B1 <= C2 and C1 <= B2):
        result = firstLargerStr
elif B1 <= A2:
    if (A1 <= B2 and C1 <= C2) or (A1 <= C2 and C1 <= B2):
        result = firstLargerStr
elif C1 <= A2:
    if (A1 <= B2 and B1 <= C2) or (A1 <= C2 and B1 <= B2):
        result = firstLargerStr

if A1 <= B2:
    if (B1 <= A2 and C1 <= C2) or (B1 <= C2 and C1 <= A2):
        result = firstLargerStr
elif B1 <= B2:
    if (A1 <= A2 and C1 <= C2) or (A1 <= C2 and C1 <= A2):
        result = firstLargerStr
elif C1 <= B2:
    if (A1 <= A2 and B1 <= C2) or (A1 <= C2 and B1 <= A2):
        result = firstLargerStr

# Second Larger
if A2 <= A1:
    if (B2 <= B1 and C2 <= C1) or (B2 <= C1 and C2 <= B1):
        result = firstLargerStr
elif B2 <= A1:
    if (A2 <= B1 and C2 <= C1) or (A2 <= C1 and C2 <= B1):
        result = firstLargerStr
elif C2 <= A1:
    if (A2 <= B1 and B2 <= C1) or (A2 <= C1 and B2 <= B1):
        result = firstLargerStr

if A2 <= B1:
    if (B2 <= A1 and C2 <= C1) or (B2 <= C1 and C2 <= A1):
        result = firstLargerStr
elif B2 <= B1:
    if (A2 <= A1 and C2 <= C1) or (A2 <= C1 and C2 <= A1):
        result = firstLargerStr
elif C2 <= B1:
    if (A2 <= A1 and B2 <= C1) or (A2 <= C1 and B2 <= A1):
        result = firstLargerStr

# Equal
if A1 == A2:
    if (B1 == B2 and C1 == C2) or (B1 == C2 and C1 == B2):
        result = equalStr
elif B1 == A2:
    if (A1 == B2 and C1 == C2) or (A1 == C2 and C1 == B2):
        result = equalStr
elif C1 == A2:
    if (B1 == B2 and C1 == C2) or (A1 == C2 and A1 == B2):
        result = equalStr

if A1 == B2:
    if (B1 == A2 and C1 == C2) or (B1 == C2 and C1 == A2):
        result = equalStr
elif B1 == B2:
    if (A1 == A2 and C1 == C2) or (A1 == C2 and C1 == A2):
        result = equalStr
elif C1 == B2:
    if (B1 == A2 and C1 == C2) or (A1 == C2 and A1 == A2):
        result = equalStr

print(result)
