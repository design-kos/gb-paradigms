numbers = [7, 3, 1, 5, 2, 8, 4, 6]

def sort_list_imperative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    
def sort_list_declarative(arr):
    return sorted(arr, reverse=True)  
    
print(sort_list_imperative(numbers))
print(sort_list_declarative(numbers))
