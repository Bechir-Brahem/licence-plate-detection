"""
script to convert from image_name,ymin,xmin,ymax,xmax similar to pascal voc but
without the class to  yolov5 image_name.txt class_id,center_x,center_y,box_w,box_h
"""

# pip install imagesize
import os
import imagesize
import glob
import argparse

parser = argparse.ArgumentParser(description='convert pascal_voc.csv format to' 
        'yolov5 format images must be stored in ./images (required to know the' 
       'width of an image)')


parser.add_argument('--source',required=True, type=str,help='the csv source'
        'file containing pascal voc labels')
parser.add_argument('--dest', type=str,help='the csv source file containing' 
       'pascal voc labels')

args = parser.parse_args()
source_file=args.source


# setup destination folder
dest_folder=args.dest
if not dest_folder:
    dest_folder='labels'

os.mkdir(dest_folder)



# fetch the size of images and store them in a dict
img_sizes={}
for img_path in glob.glob('images/*.jpg'):
    width, height = imagesize.get(img_path)
    img_sizes[img_path[7:]]=(width,height)


#read source file and iterate over its lines
f = open(source_file, "r")
text = f.read().split('\n')[1:]
for i,line in enumerate(text):
    if line == '':
        print('\nskip one')
        continue
    #split the line 
    voc=line.split(',')
    file,ymin,xmin,ymax,xmax,imw,imh=*voc,*img_sizes[voc[0]]

    #convert line variables into integers 
    arr = [xmin,ymin,xmax,ymax,imw,imh]
    arr= [ int(x) for x in arr ]
    [xmin,ymin,xmax,ymax,imw,imh]=arr

    #calculate yolo coordinates
    class_id=0
    center_x=(xmin+xmax)/(2*imw)
    center_y=(ymin+ymax)/(2*imh)
    box_w=(xmax-xmin)/imw
    box_h=(ymax-ymin)/imh
    yolo=[class_id,center_x,center_y,box_w,box_h]

    #convert values to string
    yolo=[str(x) for x in yolo]
    #convert values to a single string
    yolo_line=' '.join(yolo)
    #create a new file in the destination folder with its name as the image name without the jpg
    newf = open(os.path.join(dest_folder,file[:-4])+".txt", "w")
    newf.write(yolo_line)
    newf.close()

    print(end='\r')
    print(i+1,'/',len(text),end='')

print('done')
