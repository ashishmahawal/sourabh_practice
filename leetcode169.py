nums = [2,2,1,1,1,2,2]
def majorityelement(nums):
    num_dict = {}
    a = len(nums)//2

    for num in nums:
        if num in num_dict.keys():
            num_dict[num]+=1
        else:
            num_dict[num]=1
    for key in num_dict.keys():
        if num_dict[key]>a:
            return key