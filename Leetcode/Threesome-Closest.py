'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
    
        min_val = 2**32 # greatest int
        res_sum = None # sum which is to be returned
        
        nums.sort() 
        for i in range(len(nums)-1):
            # two pointers
            left = i+1
            right = len(nums)-1
            
            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                
                if cur_sum == target:
                    return cur_sum
                
                else:
                    cur_value = abs(target-cur_sum)
                
                    if cur_value < min_val:
                        min_val = cur_value
                        res_sum = cur_sum
                    
                    if cur_sum>target:
                        right -= 1
                    else:
                        left += 1
        return res_sum
                        
        
test = Solution()
nums = [int(num) for num in input("Space seperated ints: ").split(' ')]
target = int(input("Target: "))
print(test.threeSumClosest(nums, target))   