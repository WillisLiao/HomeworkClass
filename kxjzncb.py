filename = 'newCharList.txt'
with open (filename, mode = 'a+') as file_obj:
    data = input('data:')
    file_obj.write(data)
file_obj.close()