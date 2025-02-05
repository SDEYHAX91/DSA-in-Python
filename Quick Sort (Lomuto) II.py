def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    j = high - 1
    
    while i < j:
        while arr[i] <= pivot and i < high:
            i+=1
        while arr[j] > pivot and j > low:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] >= pivot:
        arr[i], arr[high] = arr[high], arr[i]
    
    return i
