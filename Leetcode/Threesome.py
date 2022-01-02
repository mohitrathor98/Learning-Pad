"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        
        # two pointer approach
        for i,num in enumerate(nums):
            
            # if previous number is same as current
            # then we are reiterating the same combinations
            if i>0 and nums[i-1] == num:
                continue
                
            # creating pointers
            left = i+1
            right = len(nums)-1
            
            while left<right:
                three_sum = num + nums[left] + nums[right]
                
                if three_sum>0:
                    # if sum is positive then we have to reduce it
                    # so decrease right pointer
                    right-=1
                elif three_sum < 0:
                    # increase left pointer to increase sum
                    left+=1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    # remove similar values
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                        
        return res

nums = [int(num) for num in input("Enter space seperated ints: ").split()]
print(Solution().threeSum(nums))