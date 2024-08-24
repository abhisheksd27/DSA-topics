def BinarySearch(a,value):
    l=0
    r=len(a)-1
    
    while l<=r:
        mid= l+(r-l)//2
        mid_value = a[mid]
        
        if mid_value ==value:
            return mid
        elif mid_value < value:
            l=mid+1
        else:
            r=mid-1
            
    return -1

numbers = [10, 2, 3, 5, 8, 7, 4, 9, 6]
numbers.sort() 

print(BinarySearch(numbers, 7))  # Expected output: 5