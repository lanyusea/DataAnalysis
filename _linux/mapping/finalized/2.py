from PIL import Image

blue = (0,0,255)
longitude_lt = 114.264002009
latitude_lt = 22.3367485753
longitude_rd =114.26362946
latitude_rd = 22.3363894561
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
        return '(' + str(floor) +',N'+str(self.lat)+',E' + str(self.lon)+')'

pointList = []
#counting image numbers

roomlist = []
counter = 0
#execute for every image
while(counter < 1):
    #load the image
    im = Image.open("2f.png")
    rgb_im = im.convert('RGB')
    pixel_length = float(im.size[0])
    pixel_width = float(im.size[1])
    print 'the row size is: '+str(pixel_length) #num of row
    print 'the column size is: '+str(pixel_width) #num of column

    #initialize variable
    row = 0
    column = 0
    pixelx_lt = 19
    pixely_lt = 142
    pixelx_rd = 577 
    pixely_rd = 666 
    floor = 2
    #rate for latitude
    rate_x = (latitude_lt-latitude_rd)/(pixelx_rd - pixelx_lt)
    #rate for longitude
    rate_y = (longitude_lt-longitude_rd)/(pixely_rd - pixely_lt)
    wf = open(str(floor),'w+')

    #find the bluePoint
    while row < pixel_width:
        while column < pixel_length:
            if rgb_im.getpixel((column,row)) == blue:
                longitude_bluePoint = longitude_rd + rate_y*(pixely_rd - row)
                latitude_bluePoint = latitude_rd + rate_x*(pixelx_rd - column)
                bluePoint = point (floor,latitude_bluePoint,longitude_bluePoint)
                pointList.append(bluePoint)
                print "found blue at pixel:(" + str(row) + "," + str(column) + ")" +", coordinate: ("+str(longitude_bluePoint)+","+str(latitude_bluePoint)+") at "+str(floor)+"th floor"
                wf.write(str(bluePoint)+'\n')
            column += 1
        column = 0
        row += 1
    wf.closed
    counter += 1
