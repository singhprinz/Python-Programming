# Python program to check if the input number is odd or even .
# A numer is even if divisible by 2 give a remainder of 0.
# If remainder is 1, it is odd number.


num = int(input("Enter a number :"))
if(num%2)==0:
 print("{0} is Even".format(num))
else:
   print("{0} is odd".format(num))