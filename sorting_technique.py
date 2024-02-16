def sorting_tech(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [5,8,65,1,0,2,47,35,2]
sorting_tech(arr)
print(arr)

v = sorted(arr)
print (v)
