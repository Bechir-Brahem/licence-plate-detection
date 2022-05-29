import subprocess
import cv2
import uuid
import os

IMG_PATH='images'
def detect_object(frame,filename):
    
    unique_id=str(uuid.uuid4())
    dir_path=os.path.join(IMG_PATH,unique_id)
    dir_path_abs=os.path.abspath(dir_path)
    os.mkdir(dir_path)


    source_img_path=os.path.join(IMG_PATH,unique_id,'source_'+filename)

    cv2.imwrite(source_img_path,frame)
    source_abspath=os.path.abspath(source_img_path)

    print(source_abspath)
    print(dir_path_abs)
    command=f'cd object_detection_and_ocr/yolov5 && python detect_and_ocr.py --weights ../best.pt --img 416 --conf 0.4 --source {source_abspath}  --crop --dest {dir_path_abs}/'

    print(command)
    subprocess.run(command,shell=True)
    detection=cv2.imread(os.path.join(dir_path,'detection.jpg'))
    crop=cv2.imread(os.path.join(dir_path,'crop.jpg'))

    return  detection,crop
    


