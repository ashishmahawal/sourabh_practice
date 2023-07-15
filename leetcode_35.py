# nums = [1,3,5,6]
# target= 5
# low = 0,
# high =len(nums)-1
# while low <= high:
#     mid = (low +high)//2
    
#     if nums[mid]>target:
#         high = mid -1
#     elif nums[mid]<target:
#         low = mid + 1
#     else:
#         print(mid)
# print("this target not in the given arrray")
def insertedsearch(nums,target):
    low,high=0,len(nums)-1
    while low<=high:
        mid = (low + high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid + 1
        else :
            high = mid - 1
    return mid + 1            
nums = [1,3,5,6]
target= 5
res = insertedsearch(nums,target)
print(res)