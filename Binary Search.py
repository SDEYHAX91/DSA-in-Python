def BinarySearch(arr, target):
    '''Performs Binary Search on arrays(list and tuples)
    1st parameter: Array or List
    2nd parameter: Target'''
    
    left, right = 0, len(arr) - 1 
    
    while left <= right:
        
        mid = (left + right)//2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            return mid
        
    return -1
