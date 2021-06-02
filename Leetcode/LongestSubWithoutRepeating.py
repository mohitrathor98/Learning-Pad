'''
    Given a string s, find the length of the longest substring without repeating characters.

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

    Input: s = "dvdf"
    Output: 3 (vdf)
'''

def lengthOfLongestSubstring(s: str) -> int:
    # start with a pos and go to last pos
    # iterate from first pos till a repetition is found
    # then iterate with next pos 
   
    curFixPos = 0
    curPos = 0
    endPos = len(s)
        
    count = 0
    maxCount = 0
    dic = {}
    while curFixPos < endPos and curPos < endPos:
            
        if s[curPos] not in dic:
            dic[s[curPos]] = 1
            count += 1
            curPos += 1
            
        else:
            dic = {}
                
            if maxCount < count:
                maxCount = count
                
            count = 0
                
            curFixPos += 1
            curPos = curFixPos
        
    if count > maxCount:
        return count
    return maxCount

s = input("String: ")
print(lengthOfLongestSubstring(s))