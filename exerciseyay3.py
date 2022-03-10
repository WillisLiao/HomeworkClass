import zipfile
import glob, os
fileZip = zipfile.ZipFile('zipedFile.zip', 'w')
for name in glob.glob('img/*.png'):
    print(f'{name} zipping....')
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
for name in glob.glob('img/*.jpg'):
    print(f'{name} zipping....')
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
fileZip.close()