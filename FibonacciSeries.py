n=int(input("Enter no.of elements:"))
fibSer=[0,1]
if n>2:
    for i in range(2,n):
        a=fibSer[i-1]+fibSer[i-2]
        fibSer.append(a)
print(fibSer)
