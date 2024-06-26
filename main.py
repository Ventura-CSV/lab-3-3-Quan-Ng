def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    Code Your Program here
    """
    list = [num1, num2, num3]
    
    maxinum = list[0]
    
    if (num2 > maxinum):
        maxinum = num2
    elif (num3 > maxinum):
        maxinum = num3
    
    print(f'The greates number is {maxinum}')
    ########################################
    # Do not delete the return statement
    ########################################
    return maxinum


if __name__ == '__main__':
    main()
