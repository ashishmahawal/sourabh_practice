class math:
    def __init__(self,num): 
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod  
    # we cannot use self keword to make a function because of utility function or static method
    def add(a,b):
        return a+b
    
#result = math.add(1,2)
#print(result) # output:3
a = math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(12,10))# we cannot use self keword to make a function because of utility function or static method
print(math.add(12,10))