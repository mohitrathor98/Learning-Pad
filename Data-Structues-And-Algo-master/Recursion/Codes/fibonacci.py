
def fibonacci(n):
    #code here
    if n==1 or n==2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Number: "))
print("Number at position ",num," is ",fibonacci(num))