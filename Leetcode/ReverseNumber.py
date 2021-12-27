# Reverse a given number

def reverse(x: int) -> int:
    
    # check for negative nums    
    flag = False
    if x<0:
        flag = True
        x = -x
            
    # reversing
    x = int(str(x)[::-1])
    
    # convert back into negatives
    if flag == True:
        x = -x
    
    # reversed number should be in 32-bit int range
    # i.e [-2^31, 2^31-1]
    if x not in range(-2147483648, 2147483648):
        return 0
        
    return x


num = int(input("Number: "))
print(f"Reverse is {reverse(num)}")