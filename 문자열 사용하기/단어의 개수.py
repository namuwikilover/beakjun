import re
line=input()
count = len(re.findall(r'\w+', line))
print(count)
