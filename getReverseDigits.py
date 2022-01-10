#Reverse the digits of a number using Python

def getReverse(number):
    rNum=0
    while number != 0:
        rNum = rNum*10 + number%10
        number = number//10

    return rNum
        

number = int(input("Enter a number:"))
print("Reverse of a {} is {}".format((number), getReverse(number)))
