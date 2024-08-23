def QuickSort(a):
    if len(a)<=1:
        return a
    else:
        pivote=a.pop()
        
        less_pivote=[]
        more_pivote=[]
        for i in a:
            if i <pivote:
                less_pivote.append(i)
            else:
                more_pivote.append(i)

        return QuickSort(less_pivote) + [pivote] +QuickSort(more_pivote)
    
    
# Test the function with an example array

arr = [12, 4, 78, 9, 45, 23, 56, 1, 89, 55]
sorted_arr = QuickSort(arr)
print(sorted_arr)