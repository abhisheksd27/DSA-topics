def selectionSort(a):
    
    for i in range(0,len(a)-1):
        min_ind=i
        
        for j in range(i+1,len(a)):
            if a[j] <a[min_ind]:
                min_ind=j 
                
        if min_ind != i:
            a[min_ind], a[i] =a[i],a[min_ind]
            
    return a

numbers = [10, 2, 3, 5, 8, 7, 4, 9, 6]
print(selectionSort(numbers))