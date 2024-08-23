def bubblesort(a):
    l=len(a)-1
    sorted=False
    
    while not sorted:
        sorted=True
        
        for i in range(l):
            if a[i] >a[i+1]:
                sorted=False
                a[i],a[i+1]=a[i+1],a[i]
                
    return a


print(bubblesort([64,34,25,12,22,11,90]))