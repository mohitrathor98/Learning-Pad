'''
    Find longest sub array with contigous even odd numbers
    I/p: 5
        10,12,14,7,8
    O/p: 3
'''


def maxEvenOdd(arr,n):
    
    #returns: the maximum length
    
    #code here
    beg = 0
    end = n-1
    subarray = 1
    oddFlag = -1
    evenFlag = -1
    longest = 1
    while beg <= end:
        
        if oddFlag == -1 and evenFlag == -1:
            if(arr[beg]%2 == 0):
                evenFlag = 1
            else:
                oddFlag = 1
                
        elif oddFlag == 1:
            if(arr[beg]%2 == 0):
                evenFlag = 1
                oddFlag = 0
                subarray+=1
                
            else:
                if longest < subarray:
                    longest = subarray
                subarray = 1
                
        elif evenFlag == 1:
            if(arr[beg]%2 != 0):
                evenFlag = 0
                oddFlag = 1
                subarray+=1
                
            else:
                if longest < subarray:
                    longest = subarray
                subarray = 1
        #print("{} {} {} {}".format(arr[beg],oddFlag,evenFlag,subarray))
        beg+=1
    if longest < subarray:
        longest = subarray
    return longest


n = int(input("Array Size: "))
arr = []
for i in range(n):
    arr.append(int(input("Array Element {}: ".format(i+1))))
print(maxEvenOdd(arr,n))