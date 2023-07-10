# emp_record = {
#     "name": "sourabh"
# }

# updated_data = str(emp_record)
# f = open('./resource/dat.txt','w')
# f.write(updated_data)

def createfile(data,filename):
    filePath = f'/Users/ashishmahawal/Desktop/sourabh/resource/{filename}'
    f = open(filePath,'w')
    f.write(str(data))
    print(f'Data written to file :{filename}')


emp_data = {
"name":"sourabh"
}
filename = 'sourabh_data.txt'
createfile(emp_data,filename)