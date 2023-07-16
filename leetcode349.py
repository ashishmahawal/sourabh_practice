#intersection of two array
#nums1 = [1,2,2,1]
#nums2 = [2,2]
# nums1 =[4,9,5]
# nums2 = [9,4,9,8,4]
# res=[] 
# for i in range(0,len(nums1)):
#     for j in range(0,len(nums2)):
#         if nums1[i]==nums2[j]:
#             res.append(nums1[i])            

# result= set(res)
# response = list(result)
# print(response)            

def intersection(nums1,nums2):
        res=[] 
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(nums1[i])            

        result= set(res)
        response = list(result)
        return response