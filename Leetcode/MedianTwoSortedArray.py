'''
    Given two sorted array find the median of merged array
'''

def findMedianSortedArrays(nums1, nums2) -> float:
        
    first = 0 
    second = 0
        
    merged = []
        
    while first < len(nums1) and second < len(nums2):
        if nums1[first] < nums2[second]:
            merged.append(nums1[first])
            first += 1
                
        else:
            merged.append(nums2[second])
            second+=1

    ### merging done
    median = 0.0
    n = len(merged)
    if n%2 != 0:
        median = merged[int((n+1)/2) - 1]
        
    else:
        median = merged[int((n/2)) - 1] + merged[int(n/2)]
        median /= 2
            
    return float('%.5f'%median)

# main

list1 = [1,3,6]
list2 = [2,4,5]
print(findMedianSortedArrays(list1,list2))