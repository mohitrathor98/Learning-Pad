"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # getting smallest string
        length_list = [len(s) for s in strs]
        smallest = strs[length_list.index(min(length_list))]
        
        i = len(smallest)
        res = ''

        while i != 0:
            flag = True
            for s in strs:
                # checking if smallest's matches with
                # prefix of all the word
                # if not then reduce one and check again
                if not s.startswith(smallest[0:i]):
                    flag = False
                    break
            if flag:
                res = smallest[0:i]
                break
            i -= 1
        return res
    

num = int(input(("Number of strings: ")))
print(f"Enter {num} strings")
strs = [input() for _ in range(num)]    
print(Solution().longestCommonPrefix(strs))
    
