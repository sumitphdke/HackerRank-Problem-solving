alice=input("")
bob=input("")
l1=alice.split()
l2=bob.split()
k=[int(num) for num in l1]
b=[int(num) for num in l2]
a=0
bob=0
for i in range(0,len(k)):
    if k[i]>b[i]:
        a=a+1
    elif k[i]<b[i]:
        bob=bob+1
    else:
        pass
print(a,bob)

