s = input()[::-1]
sum = 0
for i in range(len(s)):
    sum += int(s[i])*(2**i)
print(sum)