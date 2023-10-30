s="hai, best of luck5!"
l=list(s)
i=0
j=len(l)-1
while i<j:
    if l[i].isalnum():
        if l[j].isalnum():
            l[i],l[j]=l[j],l[i]
            i+=1 
            j-=1 
        else:
            j-=1 
    else:
        i+=1 
t=l
print("".join(t))

print()


a="hai, best of luck5!"
r=[a[i] for i in range(len(a)-1,-1,-1) if a[i].isalnum()]
x=0
for i in range(len(a)):
    if a[i].isalnum():
        print(r[x],end="")
        x+=1 
    else:
        print(a[i],end="")
    