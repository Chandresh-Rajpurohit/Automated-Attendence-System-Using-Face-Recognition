import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
import numpy
import os
import numpy as np
from os import listdir
from os.path import isfile ,join
import cv2,time
from csv import writer
from tkinter import messagebox,dialog
from Students_Info import Student_Data
from Attendence import Record
import pyttsx3

    
class HOME_c:

    def Home(r):

        IDLIST =[]
        root  =r
        data = []

        #Background img
        image2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\face.jpeg')
        image2 = image2.resize((1100,600),Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        label1 = tk.Label(image = image1)
        label1.place(x=0,y=0,width= 1100,height= 600)

        # text 
        text_bg= tk.Label(text ="AUTOMATED ATTENDENCE SYSTEM USING FACE RECOGNITION",font=("times new roman",25,"bold"),bg= "gold",fg= "red")
        text_bg.place(x=0,y=60,width=1100,height= 65)


        #top image _1
        bk =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facial2.jpg')
        bk_1 = bk.resize((400,60),Image.ANTIALIAS)
        bk_1 = ImageTk.PhotoImage(bk_1)
        label2 = tk.Label(image = bk_1)
        label2.place(x=0,y=0,width= 400,height= 60)

        # TOP IMAGE_2
        bk2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facialrecognition.png')
        bk_2 = bk2.resize((400,60),Image.ANTIALIAS)
        bk_2 = ImageTk.PhotoImage(bk_2)
        label3 = tk.Label(image = bk_2)
        label3.place(x=400,y=0,width= 400,height= 60)

        #top image _3
        bk3 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\images.jpg')
        bk_3 = bk3.resize((400,60),Image.ANTIALIAS)
        bk_3 = ImageTk.PhotoImage(bk_3)
        label3 = tk.Label(image = bk_3)
        label3.place(x=800,y=0,width= 400,height= 60)

        #bottom image _1
        bottonImg =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facialrecognition.png')
        bottonImg_1 = bottonImg.resize((600,70),Image.ANTIALIAS)
        bottonImg_1 = ImageTk.PhotoImage(bottonImg_1)
        label4 = tk.Label(image = bottonImg_1)
        label4.place(x=0,y=530,width= 600,height= 70)

        #bottom image _2
        bottonImg2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facialrecognition.png')
        bottonImg_2 = bottonImg2.resize((600,70),Image.ANTIALIAS)
        bottonImg_2 = ImageTk.PhotoImage(bottonImg_2)
        label5 = tk.Label(image = bottonImg_2)
        label5.place(x=600,y=530,width= 600,height= 70)

        # border 1 
        bottonImg3 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\border.jpg')
        bottonImg_3 = bottonImg3.resize((600,20),Image.ANTIALIAS)
        bottonImg_3 = ImageTk.PhotoImage(bottonImg_3)
        label6 = tk.Label(image = bottonImg_3)
        label6.place(x=0,y=510,width= 600,height= 20)

        # border 1 
        bottonImg4 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\border.jpg')
        bottonImg_4 = bottonImg4.resize((600,20),Image.ANTIALIAS)
        bottonImg_4 = ImageTk.PhotoImage(bottonImg_4)
        label7 = tk.Label(image = bottonImg_4)
        label7.place(x=600,y=510,width= 600,height= 20)


        def student_det():
            obj = Student_Data.stud_data(root)


        #student details button
        image3 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\Student_d.jpg')
        image4 = image3.resize((200,200),Image.ANTIALIAS)
        image4 = ImageTk.PhotoImage(image4)
        b1 = tk.Button(image= image4,command = student_det,cursor= "hand2")
        b1.place(x=50,y=190,width = 200,height= 200)

        b1_1 = tk.Button(text ="Student Detail",cursor= "hand2",font=("times new roman",18,"bold"),bg= "green",fg= "black")
        b1_1.place(x=50,y=390,width = 200,height= 40)



        def train_data():
            data= "E:/CHANDRESH/python/AAFR/dataset/"
            onlyFiles  =[f for f in listdir(data) if isfile(join(data,f))]

            training_data,labels = [],[]
            for i, files in enumerate(onlyFiles):
  

                image_path= data+onlyFiles[i]
                images= cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
                training_data.append(np.asarray(images,dtype=np.uint8))
                labels.append(int(os.path.split(image_path)[-1].split(".")[1]) )


            labels= np.asarray(labels) 

            model = cv2.face.LBPHFaceRecognizer_create()

            model.train(np.asarray(training_data),np.asarray(labels))

            model.save("E:/CHANDRESH/python/AAFR/training/Trainer.yml")  

            messagebox.showinfo("Train Data","Training of data is Completed")



        # train data button
        image5 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\Student.jpg')
        image6 = image5.resize((200,200),Image.ANTIALIAS)
        image6 = ImageTk.PhotoImage(image6)
        b2 = tk.Button(image= image6,command = train_data,cursor= "hand2")
        b2.place(x=320,y=190,width = 200,height= 200)

        b2_1 = tk.Button(text ="Train Data",cursor= "hand2",font=("times new roman",18,"bold"),bg= "orange",fg= "black")
        b2_1.place(x=320,y=390,width = 200,height= 40)

       #mark attendence
        def mark_att(id,name,Dept,sem,pre):
            
            row = [id,name,Dept,sem,pre]
            if id not in IDLIST :
                with open('E:\\CHANDRESH\\python\\AAFR\\Attendence\\Attendence_Record.csv','a') as csvFile:
                    writer_o = writer(csvFile)
                    writer_o.writerow(row)
                    csvFile.close()
                    IDLIST.append(id)
                    


        #face_Detection
        def face_detect():

            model = cv2.face.LBPHFaceRecognizer_create()

                # model.train(np.asarray(training_data),np.asarray(labels))
            model.read("E:/CHANDRESH/python/AAFR/training/Trainer.yml")
            face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            df=pd.read_csv('E:\\CHANDRESH\\python\\AAFR\\StudentDetail\\StudentDetails.csv')
            df.set_index("Roll_No", inplace = True)

            video_cap = cv2.VideoCapture(0)
            count = 0
            while True:

                ret, im = video_cap.read() 
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
                faces = face_cas.detectMultiScale(gray, 1.2, 5)     
                for(x, y, w, h) in faces:

                    cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2) 
                    id, conf = model.predict(gray[y:y + h, x:x + w]) 

                    if(conf < 60):
                        count = count+1
                        na = df.loc[id]
                        name = na[0] 
                        Dept = na[1] 
                        Sem = na[2]
                        tt = str(id) 
                        present = "Present"
                       
                        if count == 10 :
                            data.append(id)
                            mark_att(id,name,Dept,Sem,present)
                            engine = pyttsx3.init()  
                            text = name+" your Attendence has been Recorded"  
                            engine.say(text)   
                            engine.runAndWait()

                    else: 
                        Id ='0'   
                        name = "Unknown"             
                        tt = str(Id)             
                    cv2.putText(im, "Roll No :"+str(tt), (110, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 130, 0), 2) 
                    cv2.putText(im, "Name :"+str(name), (110, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 128, 0), 2)         
                cv2.imshow('Face Recognition', im) 

                k =  cv2.waitKey(1)

                if k == 13:
                    break
                
            
            video_cap.release()
            cv2.destroyAllWindows()

    

        #face detector button
        image7 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\a.jpg')
        image8 = image7.resize((200,200),Image.ANTIALIAS)
        image8 = ImageTk.PhotoImage(image8)
        b3 = tk.Button(image= image8,command = face_detect,cursor= "hand2")
        b3.place(x=590,y=190,width = 200,height= 200)

        b3_1 = tk.Button(text ="Face Detector",cursor= "hand2",font=("times new roman",18,"bold"),bg= "purple",fg= "black")
        b3_1.place(x=590,y=390,width = 200,height= 40)
        

        def At_re():
            if len(data) == 0:
                messagebox.showinfo("Attendence","No  Attendence Is Recorded")
            else:
                Record.Att_record(root)
       
        
        #attendence button
        image9 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\att.jpg')
        image10 = image9.resize((200,200),Image.ANTIALIAS)
        image10 = ImageTk.PhotoImage(image10)
        b4 = tk.Button(image= image10 ,command = At_re,cursor= "hand2")
        b4.place(x=860,y=190,width = 200,height= 200)

        b4_1 = tk.Button(text ="Attendence " ,cursor= "hand2",font=("times new roman",18,"bold"),bg= "brown",fg= "black")
        b4_1.place(x=860,y=390,width = 200,height= 40)


        root.mainloop()


if __name__ =="__main__":
    root = tk.Tk()
    root.title("AAFR-Automated Attendence System Using Face Recognition")
    root.geometry('1100x600+250+100')
    HOME_c.Home(root)




