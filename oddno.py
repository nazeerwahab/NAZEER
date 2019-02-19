p=input().split()
a=int(p[0])
r=int(p[1])
for i in range(a+1,r):
    if(i%2!=0):
        print(i,end=' ')
