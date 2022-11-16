z = int(input())
c = input()

if c == "k":
    a = int(input())
    z = z / 1024
    z = round(z, a)
    print(z)
else:
    z = z*1024
    print(z)