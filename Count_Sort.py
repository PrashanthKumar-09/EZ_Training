l=[1,2,3,4,5,6,7,8,9,0,0,9,8,7,6,5,4,3,2,1]#list(map(int,input().split()))
print(l)
k=[False for _ in range(10)]
print(k)
c1=c2=c3=c4=c5=c6=c7=c8=c9=c0=0
for i in range(len(l)):
    if l[i]==1:
        c1+=1
    elif l[i]==2:
        c2+=1
    elif l[i]==3:
        c3+=1
    elif l[i]==4:
        c4+=1
    elif l[i]==5:
        c5+=1
    elif l[i]==6:
        c6+=1
    elif l[i]==7:
        c7+=1
    elif l[i]==8:
        c8+=1
    elif l[i]==9:
        c9+=1
    elif l[i]==0:
        c0+=1
    else:
        pass
print("0:",c0)
print("1:",c1)
print("2:",c2)
print("3:",c3)
print("4:",c4)
print("5:",c5)
print("6:",c6)
print("7:",c7)
print("8:",c8)
print("9:",c9)
sot=list(['0 '*c0,'1 '*c1,'2 '*c2,'3 '*c3,'4 '*c4,'5 '*c5,'6 '*c6,'7 '*c7,'8 '*c8,'9 '*c9])
print(sot)
