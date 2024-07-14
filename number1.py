f=open('17.txt')
a=[int(x) for x in f]
def prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
minch=10**10
maxp=0
k=0
for i in range(len(a)):
    if a[i]<minch:
        minch=a[i]
for i in range (len(a)-1):
    if (prime(a[i])+prime(a[i+1]))>=1 and (a[i]+a[i+1])>minch:
        k+=1
        maxp=max(maxp,a[i]+a[i+1])
print(k,maxp)