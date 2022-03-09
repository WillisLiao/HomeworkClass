import os
#####3
#with open("copy.txt", "w") as file:
#    file.write("Your text goes here")
#########################################
for i in range(1, 30):

    save_path = 'C:\{}'.format(input('輸入你的路徑Users\willi\HomeworkClass'))
    file_name = 'char{}.txt'.format(i)
    completeName = os.path.join(save_path, file_name)
    print(completeName)
    file1 = open(completeName, "w")
    file1.write("fk you")
    file1.close()