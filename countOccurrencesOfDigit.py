#Count the Number of Occurrences of digit in a number using Python

def countNumberOfOccurrences(num,digit):
    count = 0
    while num != 0:
        if num%10 == digit:
            count=count+1
        num=num//10

    return count
            


num=int(input("Enter a number:"))
digit=int(input("Enter a digit:"))

print(digit,"occurred",countNumberOfOccurrences(num,digit),"times in",num)
