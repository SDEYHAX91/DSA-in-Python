import random as r

def RandomizedQuickSort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        p = partition(arr, low, high)
        RandomizedQuickSort(arr, low, p-1)
        RandomizedQuickSort(arr, p+1, high)


def partition(arr, low, high):
    p = r.randint(low,high) #Selects random index in array for pivot selection
    pivot = arr[p] #Random pivot element
    arr[low], arr[p] = arr[p], arr[low] #Pivot is swapped with first element of array
    
    i = low + 1
    j = high
    
    while True:
        while arr[i] <= pivot and i <= high:
            i += 1
        
        while arr[j] > pivot and j >= low:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
