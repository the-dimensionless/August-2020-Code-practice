import re

s = "BruceWayneIsBatman"
x = ' '.join(re.findall(".[^A-Z]*",s)).lower()
print(x)
