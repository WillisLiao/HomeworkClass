import os
pwFileName = 'newCharList.txt'
pwList = []
with open(pwFileName) as pwFile_obj:
    pwList = pwFile_obj.readlines()
pwFile_obj.close()