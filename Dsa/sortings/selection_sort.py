arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_index = i # i = 0,1,2,3,4
    for j in range(i+1,len(arr)): # j = 1,2,3,4
        if arr[j]<arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print(arr)



