def binarySearch(arr, target):
    left=0
    right=len(arr)-1
    while (left<=right):
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif(arr[mid]<target):
            left = mid +1
        else: 
            right = mid-1
    return -1 

a = [1,2,3,4,5,6]
target = 3
result = binarySearch(a, target)

if result != -1: 
    print(f"Target present at index: {result}")
else: 
    print("The target is not in the array")