n=int(input("enter any number:"))
a=0
b=1
i=0
print(a)
print(b)
c=b
print(c)
while i<=n:
    a=b
    b=c
    c=a+b
    print(c)
    i+=1
