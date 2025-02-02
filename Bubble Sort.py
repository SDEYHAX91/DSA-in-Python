def BubbleSort(lst):
    '''Perform a bubble sort on a specified list'''
    
    n = len(lst)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
  #Converts the unsorted array into sorted array
