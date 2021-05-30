# Python program to display all the prime numbers within an interval
#change the values of lower and upper for a different result
lower=900
upper=1000
#lower = iny(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))
print("Print numbers between",lower, "and", upper, "are:")
for num in range ( lower,upper,"are:"):
# prime numbers are greater than 1
        if num>1 :
            for i in range(2,num):
                if(num % i)== 0:
                    break
        else:
                print(num)