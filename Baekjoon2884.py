H, M = input().split()

Sum = int(H)*60 + int(M)
Result = (Sum - 45)
if Result < 0:
    RH = 23
    RM = Result + 60
else:
    RH = Result // 60
    RM = Result % 60

print(RH, RM)