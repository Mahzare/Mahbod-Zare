def heapify(arr, start, end):

    root = start
    while root * 2 + 1 <= end:
            child = root * 2 + 1
   
            if child + 1 <= end and arr[child] < arr[child + 1]:
                  child += 1
            if child <= end and arr[root] < arr[child]:
                  arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

def heapsort(arr):
  
    end = len(arr) - 1
    for start in range(end, -1, -1):
        heapify(arr, start, end)
    for i in range(end, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
data = [5, 2, 4, 6, 1, 3]
print("آرایه ورودی:", data)

heapsort(data)
print("آرایه مرتب شده:", data)
