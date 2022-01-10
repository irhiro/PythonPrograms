#Print the first Digit of a Number using Python

def getFirstDigit(num):

    while num != 0:
        if num//10 == 0:
            return num
        num=num//10

    


num = int(input("Enter a number: "))

print("The first digit of",num,"is",getFirstDigit(num))
