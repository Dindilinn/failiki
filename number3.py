f=open('17 (3).txt')
a=[int(x) for x in f]
def delit(n):
    d=[]
    for i in range(1,int(abs(n)**0.5)+1):
        if abs(n)%i==0:
            d.append(i)
            if i!=abs(n)//i:
                d.append(abs(n)//i)
    return len(d)-2
minim=10**10
nr=0
for i in range(len(a)):
    if a[i]<0 and abs(a[i])%5==0 and abs(a[i])%8!=0:
        minim=min(minim,a[i])
        if a[i]==minim:
            nr=i+1
maxim=-10**10
for i in range(len(a)):
    if a[i]>0 and delit(a[i])==5:
        maxim=max(maxim,a[i])
print(nr,maxim)