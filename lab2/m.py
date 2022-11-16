q = []
while(True):
    x = input().split()
    if  x[0] == "0":
        break
    q.append(x[::-1])
q.sort()
for i in range(len(q)):
    print(*q[i][::-1])


        