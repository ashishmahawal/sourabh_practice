# find min_num in the given array 
# num_list = [60,50,40,30,20,10]
# temp = num_list[0]
# for num in num_list:
#     if temp>=num:
#         temp = num
# print(temp)    
# find max_num in the given array
# new_num_list = [10,30,40,50,60,70,100]
# tmp = new_num_list[0]
# for num in new_num_list:
#     if tmp >= num:
#         tmp = num
# print(tmp)       

# here we want the search element index so we should use range function:
numbers = [10,30,40,50,60,70,100]
key = 70
for i in range(0,len(numbers)):
    if key == numbers[i]:
        print(i)       