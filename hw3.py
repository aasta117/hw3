def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        
        
        print(f"Pivot: {pivot}")
        print(f"Less than pivot: {less_than_pivot}")
        print(f"Greater than pivot: {greater_than_pivot}")
        print("-" * 40)
        
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Original array:")
print(arr)
print("\nSorting process:")
sorted_arr = quick_sort(arr)
print("\nSorted array:")
print(sorted_arr)
