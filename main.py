def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    Code Your Program here
    """
    list = [num1, num2, num3]
    
    maxnum = list[0]
    
    if (num2 > maxnum):
        maxnum = num2
    elif (num3 > maxnum):
        maxnum = num3
    
    print(f'The greates number is {maxnum}')
    ########################################
    # Do not delete the return statement
    ########################################
    return maxnum



