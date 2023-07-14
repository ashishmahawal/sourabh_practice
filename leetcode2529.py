# #maximum count of positive integer and negative integer
# numlist = [-1,-2,-3,1,2,3,4]
# respositive = 0
# resnegative = 0 

# for num in numlist:
#     if num>0:
#         respositive+=1
#     elif num<0:
#         resnegative+=1

# if respositive>resnegative:
#     print(respositive)
# else:
#     print(resnegative)    

def max_count(num_list):
    respositive = 0
    resnegative = 0     
    for num in num_list:
     if num>0:
         respositive+=1
     elif num<0:
         resnegative+=1

    if respositive>resnegative:
       return respositive
    else:
       return resnegative
    
