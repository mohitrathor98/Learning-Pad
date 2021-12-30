"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
"""

class Solution:
    
    def intToRoman(self, num: int) -> str:
        roman_dic = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        res = ""
    
        if num >= 1000:
            while num >= 1000:
                num -= 1000
                res += roman_dic[1000]
                
        if num >= 100:
            # 996 ==> extract = 900
            extract = (num//100)*100
            if extract >= 900:
                num -= 900
                res += roman_dic[100]+roman_dic[1000]
            elif extract >= 400 and extract < 500:
                num -= 400
                res += roman_dic[100]+roman_dic[500]
            elif extract>=500:
                num-=500
                extract-=500
                res+=roman_dic[500]
            
            # for 100, 200, 300
            if extract>=100 and num>=100:
                num -= extract
                res += ((extract//100)*roman_dic[100])
                
        if num>=10:
            # 96 ==> extract = 90
            extract = (num//10)*10
            if extract>=90:
                num-=90
                res += roman_dic[10]+roman_dic[100]
            elif extract >= 40 and extract<50:
                num-=40
                res += roman_dic[10]+roman_dic[50]
            elif extract>=50:
                num-=50
                extract-=50
                res+=roman_dic[50]
            
            # for 10, 20, 30       
            if extract>=10 and num>=10:
                num -= extract
                res += ((extract//10)*roman_dic[10])
        
        if num<10:        
            if num == 9:
                res += roman_dic[1]+roman_dic[10]
            elif num == 4:
                res += roman_dic[1]+roman_dic[5]
            else:
                # for 5 and 1
                if num in roman_dic.keys():
                    res += roman_dic[num]
                else:
                    # for 6, 7, 8
                    if num>5:
                        res+=roman_dic[5]
                        num-=5
                    # for 2 and 3
                    for _ in range(num):
                        num-=1
                        res+=roman_dic[1]
                
        return res

print((Solution().intToRoman(int((input("Enter a number to convert: "))))))