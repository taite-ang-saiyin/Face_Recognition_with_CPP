import sys
import subprocess
import os.path
from data import root2, image1_to_open
import cv2
import face_recognition
import numpy as np
from os import listdir
import os
import time
import imutils
import RPi.GPIO as GPIO
import threading
import h5py
from imutils.video import FPS
from Queue import Queue
from Tkinter import *
from PIL import ImageTk,Image
class FaceRec:
        def __init__(self,vs):
                self.vs=vs
                self.frame=None
                self.thread=None
                self.stopEvent=None
                self.Q=Queue(maxsize=1)
                self.root=Tk()
                self.root.title('DSSTRC')
                
                #self.root.attributes('-zoomed',True)
                self.root.attributes('-fullscreen',True)
                self.root.bind("<F11>",lambda event:self.root.attributes("-fullscreen",not self.root.attributes("-fullscreen")))
                #self.root.bind("<Escape>",lambda event:self.root.attributes("-fullscreen",False))
                
                #self.detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                self.frame = Frame(self.root, width = 1000, height=600,  highlightbackground = 'green', highlightthickness=10)
                self.frame.grid(row=0,column=0, padx=100, pady=100, ipadx=20, ipady=20)

                self.title_label = Label(self.frame,text="Face Recognition System",font=("Helvetica",30,"bold","italic"),fg="green")
                self.title_label.grid(row=0, column =1, columnspan=3,padx= 15, pady=15  )
                self.bc_label = Label(self.frame, text="BC",font=("Helvetica",20,"bold"))
                self.bc_label.grid(row=2, column=1, sticky=E)
                self.name_label = Label(self.frame, text="Name",font=("Helvetica",20,"bold"))
                self.name_label.grid(row=3, column=1, sticky=E)
                self.age_label = Label(self.frame, text="Age",font=("Helvetica",20,"bold"))          
                self.age_label.grid(row=4, column=1, sticky=E)
                self.department_label = Label(self.frame, text="Department",font=("Helvetica",20,"bold"))
                self.department_label.grid(row=5, column=1, sticky=E)

                self.bc = Entry(self.frame, width=30)
                self.bc.grid(row=2, column=2, pady=10)
                self.name = Entry(self.frame, width=30)
                self.name.grid(row=3, column=2, pady=10)
                self.age = Entry(self.frame, width=30)
                self.age.grid(row=4, column=2, pady=10)
                self.department = Entry(self.frame, width=30)
                self.department.grid(row=5, column=2, pady=10)


                self.new_btn = Button(self.frame, text="New",fg="black", bg="Moccasin", width=12,activebackground='green')#, command=new)
                self.new_btn.grid(row=6, column=2, padx=20, pady=20, sticky=W)


                self.frame1 = Frame(self.frame, width = 250, height=250,  highlightbackground = 'green', highlightthickness=5)
                self.frame1.grid(row=1,column=0, rowspan= 6, padx=20, pady=20, ipadx=20, ipady=20)

                self.frame2 = Frame(self.frame, width = 250, height=250,  highlightbackground = 'green', highlightthickness=5)
                self.frame2.grid(row=2,column=5, rowspan= 6, padx=30, pady=20, ipadx=20, ipady=20)

                self.my_label=None
                self.my_label1=None

                self.image2_to_open = os.path.join(root2, 'GIS_FaceLock.h5')
                self.hf=h5py.File(self.image2_to_open,'a')
                self.length=len(self.hf.keys())
                self.process_this_frame=True
                self.fps = FPS().start()
                self.pin1=17
                self.pin2=18
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.pin2,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.pin1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
                self.check_name=None

                self.stopEvent=threading.Event()
                self.thread=threading.Thread(target=self.videoloop,args=())
                self.thread.start()
                self.switchRecog=0
                self.root.wm_protocol("WM_DELETE_WINDOW",self.onClose)
                self.CheckImgLabel=0
        def reset(self):
                GPIO.output(self.pin2,GPIO.LOW)
                self.bc.delete(0,'end')
                self.name.delete(0,'end')
                self.age.delete(0,'end')
                self.department.delete(0,'end')
                self.check_name=''
                self.switchRecog=0
                if self.CheckImgLabel==1:
                        #self.my_label1.image=None # left image box 
                        self.my_label.image=None # Right image box
                        self.CheckImgLabel=0
                else:
                        self.my_label1.image=None
                        self.my_label.image=None
                
        def pushed(self):
                print("pushed")
                GPIO.output(self.pin2,GPIO.HIGH)
                self.switchRecog=1   
        
        def findCosineSimilarity(self,source_representation, test_representation):
                a = np.matmul(np.transpose(source_representation), test_representation)
                b = np.sum(np.multiply(source_representation, source_representation))
                c = np.sum(np.multiply(test_representation, test_representation))
                return 1 - (a / (np.sqrt(b) * np.sqrt(c)))
        '''
        def face_distance(self,face_encodings, face_to_compare):
                if len(face_encodings) == 0:
                        return np.empty((0))
                return np.linalg.norm(face_encodings - face_to_compare, axis=1)
        '''
    
        def Recog(self,image):
                #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                small_frame=cv2.resize(image,(0,0),fx=0.25,fy=0.25)
                rgb_small_frame=small_frame[:,:,::-1]
                name='Unknown'
                if self.process_this_frame:
                        face_locations=face_recognition.face_locations(rgb_small_frame)
                        #rects = self.detector.detectMultiScale(gray,scaleFactor = 1.3, minNeighbors = 5, minSize = (30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
                        #if rects is not None:
                        if face_locations is not None:
                                #face_locations = [(y, x+w, y+h, x) for (x,y,w,h) in rects]
                                face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
                                for face_encoding in face_encodings:
                                    for i in range(self.length):
                                        dataset_name=list(self.hf.keys())[i]
                                        print("dataset ",dataset_name)
                                        img_encod=np.array(self.hf[dataset_name])
                                        BC=self.hf[dataset_name].attrs['BC'].decode('utf-8')
                                        Age=self.hf[dataset_name].attrs['Age'].decode('utf-8')
                                        Dept=self.hf[dataset_name].attrs['Dept'].decode('utf-8')
                                        img_encod=np.reshape(img_encod,128)
                                        dataset_name=dataset_name.encode('ascii')
                                        face_distances=self.findCosineSimilarity(img_encod,face_encoding)
                                        print("face_distances ",face_distances)
                                        if(float(face_distances)<0.050):
                                            name=dataset_name.decode('utf-8')
                                            if(self.check_name!=name):
                                                self.check_name=name
                                                t=threading.Timer(30,self.reset)
                                                t.start()
                                                self.bc.insert(1,BC)
                                                self.name.insert(1,name)
                                                self.age.insert(1,Age)
                                                self.department.insert(1,Dept)
                                                
                                                name2 = name + '.jpg'
                                                image1_to_open2 = os.path.join(image1_to_open, name2)
                                                
                                                my_pic1 = Image.open(image1_to_open2)
                                                resized = my_pic1.resize((250,250), Image.ANTIALIAS)
                                                new_pic1 = ImageTk.PhotoImage(resized)
                                                if self.my_label1 is None:
                                                        self.my_label1 = Label(self.frame2, image=new_pic1)
                                                        self.my_label1.image=new_pic1
                                                        self.my_label1.pack(padx=20, pady=20)
                                                else:
                                                        self.my_label1.configure(image=new_pic1)
                                                        self.my_label1.image=new_pic1
                                                
                                                self.pushed()
                                                break
                self.fps.update()
                self.process_this_frame=not self.process_this_frame

        def videoloop(self):
                        try:
                                while not self.stopEvent.is_set():
                                        _,self.frame=self.vs.read()
                                        if(GPIO.input(self.pin1)==1 and self.switchRecog==0):
                                                self.pushed()
                                                self.CheckImgLabel=1
                                                t=threading.Timer(30,self.reset)
                                                t.start()
                                        
                                        self.Q.put(self.frame)
                                        self.frame=self.Q.get()
                                        image=cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
                                        image=Image.fromarray(image)
                                        image= image.resize((250,250),Image.ANTIALIAS)
                                        new_pic = ImageTk.PhotoImage(image)
                                        if self.my_label is None:
                                                self.my_label = Label(self.frame1, image=new_pic)
                                                self.my_label.image=new_pic
                                                self.my_label.pack(padx= 20, pady=20)
                                        else:
                                                self.my_label.configure(image=new_pic)
                                                self.my_label.image=new_pic
                                        if self.switchRecog == 0:
                                                self.Recog(self.frame)# size ka ahtal mhar resize lote pi thar
                        except RuntimeError, e:
                                print("Error ")
        def onClose(self):
                        self.stopEvent.set()
                        self.vs.release()
                        GPIO.cleanup()
                        self.root.quit()

