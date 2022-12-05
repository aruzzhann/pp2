import re
text = str(input())
x = re.search(r'a.*?b$', text)
if x: print("match")
else: print("not match")