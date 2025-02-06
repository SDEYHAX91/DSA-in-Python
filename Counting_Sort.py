def CountingSort(arr):
    
    isngve = False
    for i in arr: #Checks if the array has -ve value(s)
        if i < 0:
            isngve = True
            break
    
    if isngve is True: #If so, then exit from the function
        exit(arr)
    
    count = [0] * (max(arr) + 1) #Create a count array for storing frequency
    
    while len(arr) > 0: #Finding count of all elements
        val = arr.pop(0) #Reducing array size to 0
        count[val] += 1 # Stroring count to new array
    
    for i in range(len(count)):
        while count[i] > 0: 
            arr.append(i) #Sorting starts and continues
            count[i] -= 1 
