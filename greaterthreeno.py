a = raw_input("Enter 1 NUMBER: ")
b = raw_input("Enter 2 NUMBER: ")
c =raw_input("Enter 3 NUMBER: ")
if(a>b) and (a>c):
  largest=a
elif(b>a) and (b>c):
    largest=b
else:
      largest=c
print("The LARGEST NUMBER :",largest)
