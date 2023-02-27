import math
def isPrime(number):
    isPrimeNumber=True
    if (number<=1):
        return False
    elif (number == 2):
        return True
    elif (number % 2 == 0):
        return False
    else :
        for i in range(3,round(math.sqrt(number))+1,2):
            if (number % i ==0):
                return False
    return True
while 1>0:
    number = int(input("Please Enter ayour number\n"))
    if(isPrime(number)):
        print("Prime Number")
    else:
        print("Note Prime Number")