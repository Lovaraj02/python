#Binary search 
#works on sorted array to find index quickly in O(log n)
arr = [ 2, 3, 7, 7, 11, 15, 25]
low = 0
high = len(arr)-1
target = 11

while low <= high:
    mid = (low+high)//2
    if arr[mid] == target:
        print(f"target found at index {mid}")
        break
    elif arr[mid] < target:
        low = mid+1
    else:
        high = mid-1