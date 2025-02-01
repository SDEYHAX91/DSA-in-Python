def LinearSearch(arr, target):
    '''Performs linear search on any iterables except those with {key:value} pairs
    1st parameter: Iterables
    2nd parameter: Target'''
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 
