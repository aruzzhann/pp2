a, b = [int(i) for i in input().split()]
def prime(a):
    cnt = 0
    for i in range (2, a):
        if (a % i) == 0:
            cnt += 1
    if cnt > 0:
        return 0
    return 1
if a < 500 and b % 2 == 0 and prime(a):
    print("Good job!")
else:
    print("Try next time!")