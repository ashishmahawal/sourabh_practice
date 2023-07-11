my_string = "hello world"
my_list =[]
for item in my_string:
    my_list.append(item)
print(my_list)    
#list comprehension
my_string = "hello world"
my_list = [item for item in my_string]
print(my_list)
my_list = [item**2 for item in range(0,12)]
print(my_list)