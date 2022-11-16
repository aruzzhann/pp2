s = input()
t = input()
print(s.find(t), end = ' ')
if s.count(t) > 1:
    print(len(s) - 1 - s[::-1].find(t))
