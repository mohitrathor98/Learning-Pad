
def twoSum(nums,target):
    if len(nums) == 0:
        return [int]
        
    d = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in d.keys():
            return [d[rem],i]
        else:
            d[nums[i]] = i

sizeOfArray = int(input("Size of array: "))
arr = []
print("Array Elements: ")
for i in range(sizeOfArray):
    arr.append(int(input()))

target = int(input("Target: "))

result = twoSum(arr,target)

print("Required indices: ",result)