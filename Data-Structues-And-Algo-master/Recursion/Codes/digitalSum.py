
def sumOfDigits(n):
    if n<10:
        return n
        
    return n%10 + sumOfDigits(n//10)

def digitalRoot(n):
    '''
    :param n: given number 
    :return: digital root as defined
    '''
    # code here
    if n<10:
        return n
    
    return digitalRoot(sumOfDigits(n))

n = int(input("Number: "))
print("Digital Root: ",digitalRoot(n))