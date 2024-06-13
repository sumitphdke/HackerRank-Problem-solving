n=input()
s=list(map(int,input().split()))
max=max(s)
count=0
for i in s:
    if max==i:
        count+=1
    else:
        pass
print(count)
