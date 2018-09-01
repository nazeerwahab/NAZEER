num = int(input("Enter a NUMBER: "))
if num < 0:
  print("Enter a POSITIVE NUMBER")
else:
  sum = 0
  while(num > 0):
    sum += num
    num -= 1
    print("The SUM is",sum)
