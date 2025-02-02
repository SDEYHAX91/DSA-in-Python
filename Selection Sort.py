def selectionSort(arr):
  """Performs Selection Sort on array/list"""
  n = len(arr)
  
  for i in range(n-1):
    min = i #Initializing min  to its current position

    for j in range(i+1, n): #Finding minimnum value if any
      if arr[min] > arr[j]:
        min = j #Update min if smaller value found

    arr[min], arr[i] = arr[i], arr[min] #Swap minimum value to its current position
