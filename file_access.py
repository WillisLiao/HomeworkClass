import os
newDir = 'char'
j= 0
for i in range(1, 20, 5):
    j += 5
    foldName = "{}{} - {:02d}".format(newDir, i, j)
    if os.path.exists(foldName):
        print("{} fold is existed!".format(foldName))
    else:
        os.mkdir(foldName)
        print("folder {} has been created!!".format(foldName))
    print('Done!')
foldName2 = "char_20up"
if os.path.exists(foldName2):
    print("{} fold is existed!".format(foldName2))
else:
    os.mkdir(foldName2)
    print("folder {} has been created!!".format(foldName2))
print('Done!')
name = list(input(''))
print(name)
for i in range(len(name)):
    print(name[i])

# opening the file in read mode
my_file = open("newCharList.txt", "r")
  
# reading the file
data = my_file.read()
  

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace(',\n' , ' ').split(':')
  
# printing the data
print(data_into_list)
my_file.close()
done_list = []
n=-1
for i in range(len(name)):
    n+= 1
    while True:
        i+=1
        if name[n] in data_into_list[i]:
            print("ok")
            print(data_into_list[i])
            done_list.append(data_into_list[i].split())
            break
        else:
            pass
print(done_list)
            