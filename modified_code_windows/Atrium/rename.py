import os

def rename(path,old,new):
    for f in os.listdir(path):
        os.rename(os.path.join(path, f),
            os.path.join(path, f.replace(old, new)))

d = open ( 'filename','r')
count_lines = len(d.readlines())
d.close()

e = open ('filename','r')
path = "atriumModified"

for i in range(0,count_lines):
    line = e.readline().split('\t')
    roomNumber = line[0]
    coordinate = line[-1].rstrip('\n')
    rename(path, roomNumber,coordinate)
e.close()
