#Sum of Digits of the number using Python

def getSumOfDigits(number):
    sum = 0
    while number != 0:
        sum+=number%10
        number=number//10
    return sum



number = int(input("Enter a number:"))
print(f"Sum of digits of {number} is {getSumOfDigits(number)}")
