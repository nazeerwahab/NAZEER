a = int(input(""))
b = int(input(""))
c = int(input(""))
if(a>b) and (a>c):
  largest=a
elif(b>a) and (b>c):
    largest=b
elif(c>a) and (c>b):
  largest=c
print(largest)
else:
  print("Invalid")
