def fun(exp):
# str = input("enter the string:")
    stack=[]
    for p in exp:
        stack.append(p)
    c=0
    for i in range(0,len(stack)-1):
         if stack[i]=='(' :
            if stack[i]==stack[i+1]:
                c=c+1
    if c >=1:
       return 1
    else:
       return 0
exp='(1+(a+b))'
print(fun(exp))

