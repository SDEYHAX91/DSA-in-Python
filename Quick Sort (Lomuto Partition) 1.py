def QuickSort(arr, low=0, high=None): 
'''Function to perform Quick Sort'''
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high) # Pivot for partition
        QuickSort(arr, low, pivot_index - 1) # Recursion
        QuickSort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Use the first element as the pivot
    i = low + 1 #Checks for value greater than pivot
    j = high #Checks for value less than pivot

    while True: 
        while i <= high and arr[i] <= pivot: #Incrementing i till element >= pivot found
            i += 1

        while j >= low and arr[j] > pivot: #Decrementing j till element <= pivot found
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] #Swap1
        else:
            break #Loop breaks if j <= i

    arr[low], arr[j] = arr[j], arr[low] #Swap pivot with arr[j](lesser element) 
    return j
