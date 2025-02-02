def BubbleSort(lst):
    '''Perform a bubble sort on a specified list'''
    
    n = len(lst)
    swapped = False
    
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped: #If given array is sorted in one go, then no need to run more
            break
