def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr = list(map(int, input("Enter numbers to be sorted: ").split()))
print("Unsorted array: ",arr)
bubble_sort(arr) #pass by object reference, hence the array gets updated in the function
print("Sorted Array: ",arr)
