import re
text = str(input())
x = re.findall('[A-Z][^A-Z]*', text)
print(x)