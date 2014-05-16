import os

def rename(path,old,new):
    for f in os.listdir(path):
        os.rename(os.path.join(path, f),
            os.path.join(path, f.replace(old, new)))

d = open ( 'filename','r')
count_lines = len(d.readlines())
d.close()

e = open ('filename','r')
path = "floor2Modified" #MODIFIED
#path is the folder that holds all files that to be renamed
#both absolute/relative path is ok
#e.g. both rename.py and folder are in ~/
#path="~/folder/files"
#or
#path="files"

rename (path, 'RM'or'rm','')
#I remove the RM or rm in the file's name first because of the content of "filename" 

for i in range(0,count_lines):
    line = e.readline().split('\t')
    roomNumber = line[0]
    coordinate = line[-1].rstrip('\n')
    rename(path, roomNumber,coordinate)
e.close()
