def MergeSort(arr): 
    '''Performs Merge sort on array/ list'''
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2 #Finds midpoint
    lefthalf = arr[mid:]  #Division
    righthalf = arr[:mid] 
    L = MergeSort(lefthalf)  #Recursive merge sort on subarrays
    R = MergeSort(righthalf) 
    
    return Merge(L,R) #Merge function

def Merge(left, right):
    """Merging of 2 sorted subarrays
    into a single sorted array"""
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right): #Comparing and appending values from both the subarrays
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res.extend(left[i:]) #Appending Remaining elements
    res.extend(right[j:])
    
    return res #O/P
