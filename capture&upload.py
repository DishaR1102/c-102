import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time = time.time()

def take_SnapShot():
    number=random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = VideoCaptureObject.read()
        img_name = 'img'+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result = False 
    return img_name 
    print("snapshot taken")
    VideoCaptureObject.release
    cv2.destroyAllWindows

def upload_File(img_name):
    access_token =  "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"
    file = img_name
    file_from = file
    file_to = '/testFolder/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_SnapShot()
            upload_file(name)

main()

