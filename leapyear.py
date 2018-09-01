year =int(input("Enter YEAR:"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a LEAP YEAR".format(year))
       else:
           print("{0} is not a LEAP YEAR".format(year))
   else:
       print("{0} is a LEAP YEAR".format(year))
else:
   print("{0} is not a LEAP YEAR".format(year))

  
