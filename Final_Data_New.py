#usage python Final_Data_New.py --NewPeople Phyo.jpg
# Timer interrupt nae par
import face_recognition
import numpy as np
import cv2
#from PIL import Image
import argparse
from os import listdir
import os
import time
import imutils
#import RPi.GPIO as GPIO
import threading
import h5py
import numpy as np
from imutils.video import FPS
import dlib
from imutils import face_utils
'''
camera = cv2.VideoCapture(0)
camera.release()
g=h5py.File('test.h5','r')
dataset_name=list(g.keys())[0]
print("data ",dataset_name)
print('feature',g[dataset_name].attrs['Feature'])
print(g[dataset_name].attrs['BC'])
print(g[dataset_name].attrs['Age'])
print(g[dataset_name].attrs['Dept'])
cv2.imshow('Img ',np.array(g[dataset_name]))
cv2.waitKey(0)
'''
'''
name='kyaw'
data1=[10,20,30,40,50]
print(data1)
def get_all(n):
        print(n)
        
hf=h5py.File('test.h5','a')
image=cv2.imread("kyaw.jpg")
face_locations=face_recognition.face_locations(image)
face_encodings=face_recognition.face_encodings(image,face_locations)
g=hf.create_dataset(name,data=image)
print(type(face_encodings),'len ',len(face_encodings))
g.attrs['Feature']=np.array(face_encodings)
BC=raw_input('BC Number ')
g.attrs['BC']=BC
Age=raw_input('Age ')
g.attrs['Age']=Age
Dept=raw_input('Department ')
g.attrs['Dept']=Dept
hf.close()


g=h5py.File('test.h5','r')
dataset_name=list(g.keys())[0]
print(np.array(g[dataset_name]))
print(g[dataset_name].attrs['Feature'])
print(g[dataset_name].attrs['BC'])
print(g[dataset_name].attrs['Age'])
print(g[dataset_name].attrs['Dept'])
cv2.imshow('Img ',np.array(g[dataset_name]))
cv2.waitKey(0)

'''

camera = cv2.VideoCapture(0)
hf=h5py.File('GIS_FaceLock.h5','a')
#detector=dlib.get_frontal_face_detector()
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
fps = FPS().start()
count=0
while True:
        (grabbed, frame) = camera.read()
        if not grabbed:
                break
        frame = imutils.resize(frame, width = 500)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rects=detector.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in rects:#for (i,rect) in enumerate(rects):
                        #shape=predictor(gray,rect)
                        #shape=face_utils.shape_to_np(shape)
                        
                        #(x,y,w,h)=face_utils.rect_to_bb(rect)
                        img=frame[int(y):int(y+h), int(x):int(x+w)]
                        if cv2.waitKey(1) & 0xFF == ord("q"):
                                try:
                                        face_locations=face_recognition.face_locations(frame)
                                        face_encodings=face_recognition.face_encodings(frame,face_locations)
                                        Name=raw_input("Enter Name ")
                                        #g=hf.create_dataset(Name,data=len(hf.keys())+1)
                                        #g=hf.create_dataset(Name,data=img)
                                        #g.attrs['Feature']=face_encodings
                                        g=hf.create_dataset(Name,data=face_encodings)
                                        BC=raw_input('BC Number ')
                                        g.attrs['BC']=BC
                                        Age=raw_input('Age ')
                                        g.attrs['Age']=Age
                                        Dept=raw_input('Department ')
                                        g.attrs['Dept']=Dept
                                        count=1
                                        filepath='Read'+'/'+Name+'.jpg'
                                        cv2.imwrite(filepath,img)
                                except:
                                        print("Can't Encode Please Try Again")
                                        count=0
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)
                        cv2.imshow("Face ",frame)
        if count==1:
                break
        fps.update()
        
hf.close()
camera.release()
cv2.destroyAllWindows()

'''
g=hf.create_group('Name')
d=g.create_dataset('default',data=name)
g.attrs['Name']=name
g.attrs['Data']=data1
g.attrs['BC']='46033'
g.attrs['Age']=33
#hf.close()
#g=h5py.File('test.h5','r')
for k in g.attrs.keys():
        print('{} => {}'.format(k,g.attrs[k]))
print("hi ",g)
hf.close()
g=h5py.File('test.h5','r')
data=g.atervalues()
print(data)
'''
'''
hf=h5py.File('test.h5','w')
#g=hf.create_dataset(name,data=data1)
g=hf.create_group('Name')
bc=g.create_group('BC')
age=bc.create_group('Age')
Names=g.create_dataset('default',data=name)
BCN=bc.create_dataset('default',data='46033')
AGEN=age.create_dataset('default',data='33')
hf.close()
hf=h5py.File('test.h5','r')
name=hf.keys()[0]
print(name)
data=hf['Name/default']
print('data is ',data)

hf.close()
'''
'''
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--NewPeople", required=True,help="path to models directory")
args = vars(ap.parse_args())
'''
#One photo to append
'''
#cap = cv2.VideoCapture(0)
path = args['NewPeople']
hf=h5py.File('data_employee_415.h5','a')
img=cv2.imread(path)
img_encod=face_recognition.face_encodings(img)[0]
length=len(path)
People=path[:length-4]
print("People ",People)
hf.create_dataset(People,data=img_encod)
hf.close()
# 
#All photo to append
Know_pictures = args['NewPeople']
Names=[]
hf=h5py.File('data_employee_415.h5','a')
for dirname, dirnames, filenames in os.walk(Know_pictures,topdown=False):
	for subdirname in filenames:
		combine=dirname;
		combine=combine+'/'
		combine=combine+subdirname
		length=len(subdirname)
		People=subdirname[:length-4]
		img2=cv2.imread(combine)
		img2 = imutils.resize(img2, width = 224)
		img_encod=face_recognition.face_encodings(img2)[0]
		Names.append(People)
		print("People ",People)
		hf.create_dataset(People,data=img_encod)
print('/n/n',Names)
hf.close()
'''
