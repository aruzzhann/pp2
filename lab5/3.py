import re
text = str(input())
x = re.search(r'^[a-z]+_[a-z]+$', text)
if x: print("match")
else: print("not match")