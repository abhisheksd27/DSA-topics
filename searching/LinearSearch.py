def linear_search(arr, target):
    # Iterate over the array
    for i in range(len(arr)):
        # Check if the current element is the target
        if arr[i] == target:
            # Return the index of the target element
            return i
    # If the target is not found, return -1
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
