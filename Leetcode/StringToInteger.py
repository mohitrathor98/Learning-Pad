'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1) Read in and ignore any leading whitespace.
2) Check if the next character (if not already at the end of the string) is '-' or '+'. 
   Read this character in if it is either. This determines if the final result is negative or positive respectively. 
   Assume the result is positive if neither is present.
3) Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
   Change the sign as necessary (from step 2).
5) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
   Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6) Return the integer as the final result.
'''

import string

def atoi(s:str) -> int:
    # remove white spaces
    s = s.strip()
   
    if len(s) == 0:
        return 0
    
    # check for + and -:
    negative = False
    i = 0
    if s[i] == "-":
        negative = True
        s = s[i+1:]
    elif s[i] == "+":
        s = s[i+1:]
    
    # read until non-digit
    res = 0
    while (i < len(s)) and (s[i] in string.digits):
        res = (res*10) + int(s[i])
        i += 1
        
    # change signs if negative
    if negative:
        res = -res
        
    # check for 32-bit range
    if res < -2147483648:
        res = -2147483648
    if res > 2147483647:
        res = 2147483647
        
    return res

print(atoi(input("String to convert: ")))