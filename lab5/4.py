import re
text = str(input())
x = re.search(r'[A-Z]+[a-z]+$', text)
if x: print("match")
else: print("not match")