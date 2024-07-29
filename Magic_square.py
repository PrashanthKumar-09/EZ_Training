ms=[[4,3,8,],[9,5,1],[2,7,6]]
s=sum(ms[0])
ns=0

for i in range(len(ms)):
    ns+=ms[i][0]
if s==ns:
    for i in range(1,len(ms)):
        f=True
        if sum(ms[i])!=s:
            f=False
            break
        cs=0
        for j in range(len(ms)):
            cs+=ms[j][i]
        if cs!=s:
            f=False
            break
    dl=0
    dl2=0
    for i in range(len(ms)):
        dl+=ms[i][i]
    for i in range(len(ms)):
        dl2+=ms[i][len(ms)-1-i]
    if dl!=s and dl2!=s:
            f=False
    if f:
        print(True)
    else:
        print(False)
else:
    print(False)