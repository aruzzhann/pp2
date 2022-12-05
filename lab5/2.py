import re
text = str(input())
x = re.search(r'ab{2,3}', text)
if x: print("match")
else: print("not match")