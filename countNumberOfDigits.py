#Count the number of digits in a Number in Python


def countNumberOfDigits(num):
    
    count=0   
    while num != 0:
        count=count+1
        num=num//10
        
    return count    


num = int(input('Enter number to count its digits: '))
print("Number of digits in the number is ",countNumberOfDigits(num))
