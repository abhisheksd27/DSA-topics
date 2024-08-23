def insertionSort(a):
    for i in range(1, len(a)):  # Start with the second element
        value_to_sort = a[i]    # Store the current element to be sorted
        
        # Move elements of a[0..i-1] that are greater than value_to_sort to one position ahead
        while a[i-1] > value_to_sort and i > 0:
            a[i], a[i-1] = a[i-1], a[i]  # Swap the elements if the previous one is greater
            i = i - 1  # Move one step back in the list to continue checking
        
    return a  # Return the sorted array

# Test the function

unsorted_array = [5, 3, 8, 2, 1, 4, 7]
print("Unsorted array:", unsorted_array)
sorted_array = insertionSort(unsorted_array)
print("Sorted array:", sorted_array)