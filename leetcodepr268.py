nums=[3,0,1]
actual =list(range(0,len(nums)+1))
res = set(actual)-set(nums)
array=list(res)
missing_number =array[0]
print(missing_number)