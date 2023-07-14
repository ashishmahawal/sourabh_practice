#maximum count of positive integer and negative integer
numlist = [-1,-2,-3,1,2,3,4]
respositive = 0
resnegative = 0 

for num in numlist:
    if num>0:
        respositive+=1
    elif num<0:
        resnegative+=1
    elif resnegative>respositive:
        print(resnegative)
    else:
        respositive> resnegative
        print(respositive)
    