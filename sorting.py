#
#find the min value first
#min_num = min(num_list)
# print(min_num)
#min_index = num_list.index(min_num)
#print(min_index)
#num_list[0],num_list[min_index]=num_list[min_index],num_list[0]
# print(num_list)
# for i in range(len(num_list)):
#     min_num = min(num_list[i:])
#     min_index = num_list.index(min_num)
#     num_list[i],num_list[min_index]=num_list[min_index],num_list[i]
# print(num_list)    





# nums = [5,3,4,2,1]
# min_num = min(nums)
# min_num_index = nums.index(min_num)
# nums[0],nums[min_num_index]=nums[min_num_index],nums[0]
# for i in range(len(nums)):
#     min_num = min(nums[i:])
#     min_num_index = nums.index(min_num)
#     nums[i],nums[min_num_index]=nums[min_num_index],nums[i]
# print(nums)  


def sort(nums):
    for i in range(len(nums)):
      min_num = min(nums[i:])
      min_num_index = nums.index(min_num)
      nums[i],nums[min_num_index]=nums[min_num_index],nums[i]
    return nums

num_list = [2,34,5,6,7,1,0]
new_list = sort(num_list)
print(new_list)