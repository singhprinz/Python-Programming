num1=14
num2=15
num3=13
if(num1>=num2) and (num1>=num3):
    if (num2 >= num1) and (num2 >= num3):
        largest = num1
    else:
        largest = num2
else:
    largest = num3
    print("the largest number between",num1,",",num2,"and",num3,"is",largest)