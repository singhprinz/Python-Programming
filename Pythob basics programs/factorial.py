#change the value for a different result
num=7
#num = iny(input("ENter a number"))
factorial =1
# check if the number is negative, posotive and zero
if num<0:
    print("Soory,factorial does not exist for negative numbers")
    if num == 0:
        print("Factorialof 0 is 1")
    else:
        for i in range(1,num+1):
                factorial=factorial*i
                print("the factorial of",num ,"is", factorial)