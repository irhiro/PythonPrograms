#Product of Digits of the number using Python

def getProductOfDigits(number):
    multiplication = 1

    while number != 0:
        
        multiplication*=number%10
        number = number//10      

    return multiplication


number = int(input("Enter a number:"))

print("The product of digits of {} is {}".format(number,getProductOfDigits(number)))
