import hashlib


outFileName = 'hashPWFile.txt'
with open(outFileName, mode='a+') as outFile_obj:
    data = input('pw: ')
    hash_obj = hashlib.md5(data.encode())
    outFile_obj.write(hash_obj.hexdigest())
    print(f'"{data}" after hash is "{hash_obj.hexdigest()}"')
outFile_obj.close()