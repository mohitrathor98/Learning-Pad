'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def __init__(self) -> None:
        pass
    
    def convert(self, s: str, numRows: int) -> str:
        
        rows = [[] for i in range(numRows)]

        i = 0
        while i != len(s):
            flag = False
            # appending values in straight order
            # to each row
            for j in range(numRows):
                rows[j].append(s[i])
                i += 1
                if i == len(s):
                    flag = True
                    break
            if flag is True:
                break
            
            # appending values to the back rows(rows-2 to 1)
            for j in range(numRows-2, 0, -1):
                rows[j].append(s[i])
                i += 1
                if i == len(s):
                    flag = True
                    break
            if flag is True:
                break
        
        zigzag = ""
        for row in rows:
            zigzag += ''.join(row)
        
        return zigzag
    
solution = Solution()
print(solution.convert(input("String: "), int(input("Number of rows: "))))