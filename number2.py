f=open('17 (2).txt')
a=[int(x) for x in f]
povt=[0]*1000000
maxim=0
for i in range(len(a)):
    povt[a[i]]+=1
    if povt[a[i]]>maxim:
        maxim=povt[a[i]]

res=[]
for i in range(len(a)):
    if povt[a[i]]==maxim:
        res.append(a[i])

print(len(set(a)),min(res))

