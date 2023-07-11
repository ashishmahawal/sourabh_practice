def binary_search(list,key):
    low =0,
    high = len(list)-1
    while low <= high:
        mid=(low+high)//2
        if list[mid]>key:
            high = mid - 1
        elif list[mid]<key:
            low = mid + 1
        else:
            return mid
    return -1       
my_list = [1,2,3,4,5,6,7,8,9]
seach_value = 5
res = binary_search(my_list,seach_value)
print(res)