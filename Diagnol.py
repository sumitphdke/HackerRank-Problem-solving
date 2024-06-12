s=[]
n=int(input())
sum1=0
sum2=0
for i in range(n):
    s.append(list(map(int,input().split())))
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if i==0:
            if j==0:
                sum1=s[i][j]+sum1
            elif j==2:
                sum2=s[i][j]+sum2
            else:
                pass
        elif i==1:
            if j==1:
                sum1=sum1+s[i][j]
                sum2=sum2+s[i][j]
        elif i==2:
            if j==0:
                sum2=sum2+s[i][j]
            elif j==2:
                sum1=sum1+s[i][j]
diff=sum1-sum2
print(abs(diff))
