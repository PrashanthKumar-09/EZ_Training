j={20:2,12:1,16:2,11:1,9:2,24:3,27:3}
l=list(j.items())
sorted_list=sorted(l,key=lambda x:x[1])
p=max(sorted_list)[0]+min(sorted_list)[0]
print(p)
# for i in sorted_list:
#     print(max(t[i]))