sum=0
import re
pattern = r'(\d+)'
k=input("")
s=input("")
match=re.findall(pattern,s)
for i in match:
    sum=sum+int(i)
print(sum)
