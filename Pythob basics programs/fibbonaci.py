# print fibbonacci series
nterms =10
#nterms = int (input("How many terms? "))
n1=0
n2=1
count=0
if nterms <= 0:
    print("please  enter a positive numebr")
    if nterms == 1:
        printf("fibonacci sequence upto",nterms,":")
        print(n1)
        else: 
            print("Fibonacci sequesncce upto ", nterms, ":")
            while count < nterms:
                print(n1, end=',')
                nth= n1 + n2