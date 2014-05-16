from PIL import Image 

blue = (0,0,255)
longitude_lt = 114.264205
latitude_lt = 22.338673
longitude_rd = 114.262969
latitude_rd = 22.3375
pixel_length = 0.0
pixel_width = 0.0
longitude_bluePoint = 0.0
latitude_bluePoint = 0.0

#initialize with form(floor, long, lat)
class point:
    def __init__(self,floor,latitude,longitude):
        self.floor = floor
        self.lon = longitude
        self.lat = latitude
    def __str__(self):
        return str(floor) +'_N'+str(self.lat)+'_E' + str(self.lon)

pointList = []
#counting image numbers

e = open ('imagefile','r')
count_lines = len(e.readlines())
e.closed

roomlist = []
counter = 0
#execute for every image
f = open ('imagefile','r')
while(counter < count_lines):
    element = f.readline().split(';')
    element[-1] = element[-1].rstrip('\n')
    print 'processing the '+ str(counter+1)+'th image: '+element[0]

    #load the image
    im = Image.open(element[0])
    rgb_im = im.convert('RGB')
    pixel_length = float(im.size[0])
    pixel_width = float(im.size[1])
    print 'the row size is: '+str(pixel_length) #num of row
    print 'the column size is: '+str(pixel_width) #num of column

    #initialize variable
    row = 0
    column = 0
    pixelx_lt = int(element[1])
    pixely_lt= int(element[2])
    pixelx_rd = int(element[3])
    pixely_rd= int(element[4])
    floor = element[5]
    roomNumber = 0
    roomlist_before = element[6].split(',')
    roomlist_b = [item.replace("RM","") for item in roomlist_before]
    roomlist = [item.replace('"','') for item in roomlist_b]
    #rate for latitude
    rate_x = (latitude_lt-latitude_rd)/(pixelx_rd - pixelx_lt)
    #rate for longitude
    rate_y = (longitude_lt-longitude_rd)/(pixely_rd - pixely_lt)
    wf = open(floor,'w+')

    #find the bluePoint
    while row < pixel_width:
        while column < pixel_length:
            if rgb_im.getpixel((column,row)) == blue:
                longitude_bluePoint = longitude_rd + rate_y*(pixely_rd - row)
                latitude_bluePoint = latitude_rd + rate_x*(pixelx_rd - column)
                bluePoint = point (floor,latitude_bluePoint,longitude_bluePoint)
                pointList.append(bluePoint)
                print "found blue at pixel:(" + str(row) + "," + str(column) + ")" +", coordinate: ("+str(longitude_bluePoint)+","+str(latitude_bluePoint)+") at "+str(floor)+"th floor"
                wf.write(str(roomlist[roomNumber])+'\t'+str(bluePoint)+'\n')
                roomNumber += 1
            column += 1
        column = 0
        row += 1
    wf.closed
    counter += 1
f.closed
