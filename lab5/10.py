import re
text = input()
pattern = re.sub('([A-Z][a-z]+)', r'\1_\2', text)
print(pattern.lower())