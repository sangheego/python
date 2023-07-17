import zipfile

filelist=['./new.txt','./data.test.txt']
with zipfile.ZipFile('./new.txt','w') as myzip:
    for temp in filelist:
        myzip.write(temp)
#압축해제
zipfile.ZipFile(',/new.txt').extractall()
