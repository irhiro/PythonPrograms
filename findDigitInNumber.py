#Find given number is a digit in a number using Python

def findDigitInNumber(num,digit):
    """
    numList = []

    while num != 0:
        numList.append(num%10)
        num=num//10

    if digit in numList:
        return True
    """

    while num != 0:
        if num%10 == digit:
            return True

        num=num//10
    return False
    


num=int(input("Enter the number: "))
digit=int(input("Enter the digit: "))

if findDigitInNumber(num,digit) is True:
    print(digit,"is occured in",num)

else:
    print(digit,"is not occured in",num)
