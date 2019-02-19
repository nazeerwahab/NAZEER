b=int(input())
list=[]
for i in range(1,6):
	mul=b*i
	list.append(mul)
print(" ".join(map(str,list)))
