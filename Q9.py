def find_idx(list1 , n):
    left = 0
    right = len(list1) -1 

    while left <= right:
        mid = (left+right) //2

        if list1[mid] == n:
            return mid
        elif list1[mid]<n:
            left = mid+1
        else:
            right = mid-1 
    return left
    


list1 = [1,2,3,4,5]
n = 6
v = find_idx(list1, n)
print(v)