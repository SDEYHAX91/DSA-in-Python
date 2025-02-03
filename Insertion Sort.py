def insertionSort(arr):
    
    for i in range(1, len(arr)): #loop for the unsorted part
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key: #loop for the sorted part
            arr[j+1] = arr[j] #moving value to its current position
            j -= 1
        
        arr[j+1] = key
