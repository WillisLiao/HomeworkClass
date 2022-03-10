import zipfile
zipFileName = input('zip file name: ')
listZipInfo = zipfile.Zipfile(zipFileName)
print(listZipInfo.namelist())