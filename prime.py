yes=False
n=int(input(""))
for i in range(2,100):
    if n!=i and n%i==0:
        yes=True
    else:
        pass
if yes==False:
    print("its a prime number")
else:
    print("not a prime number")
