def merge2sortedList(arr1, arr2):
'''Merge two sorted lists into a sorted list
parameter 1: list,
parameter 2: list'''

    i,j =0,0
    merged = []
    
    while i < len(arr1) and j < len(arr2): #Comparing smaller values from subarrays and inserting them in new array
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
        
        merged.extend(arr1) #Inserting remaining elements into the final array 
        merged.extend(arr2)
    
    return merged
