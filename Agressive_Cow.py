n=4
m=[1,3,4,7,9,11,12,14]
l=[]
for i in range(len(m)-1):
    x=(m[i]-m[i+1])*-1
    print(x,end=' ')
    l.append(x)
print()
print(l)
print(max(l))
if max(l)>n:
    print(n)
else:
    print(max(l))