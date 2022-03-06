import os
pwFileName = 'paswrd.txt'
with open (pwFileName) as pwFile_obj:
    for line in pwFile_obj:
        print(line.rstrip())      
pwFile_obj.close()