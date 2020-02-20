#Input ='cat dog god tca'
#Output : [[1, 4], [2, 3]]
def str(Input):
    l=['dummy']
    lis=(Input.split(" "))
    for i in lis:
         l.append(i)
    li=[]
    for i in range(0,len(l)-1):
          for j in (i+1,len(l)-1):
                if (sorted(l[i]) == sorted(l[j])):
                       li.append([l.index(l[i]),l.index(l[j])])
    return li
Input ='cat dog god tca spar rasp'
print(str(Input))



