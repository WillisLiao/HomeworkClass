import os
save_path = 'C:\{}'.format(input('書你的路徑Users\willi\HomeworkClass'))
file_name = 'test.txt'
completeName = os.path.join(save_path, file_name)
print(completeName)
file1 = open(completeName, "w")
file1.write("fk you")
file1.close()