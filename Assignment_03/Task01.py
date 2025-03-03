# Calculating factorial

def factorial(num):

    if(num <= 1):
        return 1
    else:
        return num * factorial(num-1)

print("Enter number : ")
num = int(input())
fact = factorial(num)
print("Factorial of ", num, " is ", fact)
