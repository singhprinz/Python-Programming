# Python program to check if the input number is prime or not
num=407
#@num=int(input("Enter a number:")
if num > 1 :
    for i in range(2,num) :
        if(num%i) == 0 :
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"is a prime number")
            # if input number is less tha or equal to 1,it is not prime
    else:
        print(num,"is not a prime number")

















