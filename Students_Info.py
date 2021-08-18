import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
import numpy 
import os
import numpy as np
from os import listdir
from os.path import isfile ,join
import cv2
from csv import writer
from tkinter import messagebox,dialog





class Student_Data:

    def stud_data(r):

        root= r
        
        face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        #top image _1
        bk =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facial2.jpg')
        bk_1 = bk.resize((400,80),Image.ANTIALIAS)
        bk_1 = ImageTk.PhotoImage(bk_1)
        label2 = tk.Label(image = bk_1)
        label2.place(x=0,y=0,width= 400,height= 80)

                # TOP IMAGE_2
        bk2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\facialrecognition.png')
        bk_2 = bk2.resize((400,80),Image.ANTIALIAS)
        bk_2 = ImageTk.PhotoImage(bk_2)
        label3 = tk.Label(image = bk_2)
        label3.place(x=400,y=0,width= 400,height= 80)

                #top image _3
        bk3 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\images.jpg')
        bk_3 = bk3.resize((400,80),Image.ANTIALIAS)
        bk_3 = ImageTk.PhotoImage(bk_3)
        label3 = tk.Label(image = bk_3)
        label3.place(x=800,y=0,width= 400,height= 80)

                #STUDENT TITLE
        text_bg= tk.Label(text ="STUDENT DETAILS",font=("times new roman",35,"bold"),bg= "orange",fg= "purple",bd = 12)
        text_bg.place(x=0,y=80,width=1100,height= 60)


                #main frame
        main_Frame = tk.Frame(bg= "white")
        main_Frame.place(x=0,y=130,width= 1100,height= 600)

                #Background img
        image2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\face.jpeg')
        image2 = image2.resize((1100,500),Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        label1 = tk.Label(main_Frame,image = image1)
        label1.place(x=0,y=0,width= 1100,height= 500)

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

                #lftFrame
        left_frame = tk.LabelFrame(main_Frame,bd =4, text = "Student Details", font=("times new roman",15,"bold"),fg= "red")
        left_frame.place(x= 220,y= 32,width= 550,height= 330)

                #student_Label
        Student_name= tk.Label(left_frame,text ="Student Name",font=("times new roman",19,"bold"),fg= "blue")
        Student_name.grid(row = 0,column = 0,padx = 14,pady= 7)
                #student_text
        Student_n = ttk.Entry(left_frame,font=("times new roman",19,"bold"))
        Student_n.grid(row= 0,column = 1,padx = 18,pady= 7)

                #roll NO_Label
        roll_no= tk.Label(left_frame,text ="Roll No",font=("times new roman",19,"bold"),fg= "blue")
        roll_no.grid(row = 1,column = 0,padx = 4,pady= 10)
                #rOLL NO TEXT
        roll_no_text = ttk.Entry(left_frame ,font=("times new roman",19,"bold"))
        roll_no_text.grid(row= 1,column = 1,padx = 8,pady= 7)

                #Dep_label
        dept= tk.Label(left_frame,text ="Department",font=("times new roman",19,"bold"),fg= "blue")
        dept.grid(row = 2,column = 0,padx = 7,pady= 10)
                #Dept. TEXT
        dept_text = ttk.Entry(left_frame,font=("times new roman",19,"bold"))
        dept_text.grid(row= 2,column = 1,padx = 8,pady= 7)


                #sem_label
        sem= tk.Label(left_frame,text ="Semester",font=("times new roman",19,"bold"),fg= "blue")
        sem.grid(row = 3,column = 0,padx = 7,pady= 10)
                #sem_TEXT
        sem_text = ttk.Entry(left_frame,font=("times new roman",19,"bold"))
        sem_text.grid(row= 3,column = 1,padx = 8,pady= 7)

        #take images
        def take_images():
            
            video_cap = cv2.VideoCapture(0)

            count = 0
            while True:
                check,frame = video_cap.read()
                if face_extractor(frame) is not None:


                    count = count+1
                    face =cv2.resize(face_extractor(frame),(500,500))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                
                    file_nae_path = "E:\\CHANDRESH\\python\\AAFR\\dataset\\"+Student_n.get()+"."+str(roll_no_text.get())+"."+str(count)+".jpg"
                    #file_nae_path = "C:\\Users\\Sanjay\\Desktop\\CHANDRESH\\python\\dataset\\"+str(count)+".jpg"
                    cv2.imwrite(file_nae_path,face)

                    cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.imshow("face cropper",face)
            
                else:

                    print("face not found")
                    pass

                if cv2.waitKey(1) == 13 or count == 100 :
                    break

            video_cap.release()
            cv2.destroyAllWindows()


        def face_extractor(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cas.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

            if faces is():
                return None

            for x,y,w,h in faces:
                cropped_img = img[y:y+h ,x:x+w]
            
            return cropped_img
                            
                                
        # take images button
        take_image= tk.Button(left_frame,text= "Take Image",command = take_images,font=("times new roman",19,"bold"),bg ="yellow")
        take_image.place(x= 40,y=230,width = 130,height= 50)

        #save data function
        def Save_Data():
            if(Student_n.get()=="" or roll_no_text.get()=="" or dept_text.get()=="" or sem_text.get()==""):
                messagebox.showinfo("Result","Enter the details")
            else:

                row = [roll_no_text.get(),Student_n.get(),dept_text.get(),sem_text.get()]
                with open('E:\\CHANDRESH\\python\\AAFR\\StudentDetail\\StudentDetails.csv','a') as csvFile:
                    writer_o = writer(csvFile)
                    writer_o.writerow(row)
                    csvFile.close()

                messagebox.showinfo("Result","Data is added successfully")

                Student_n.delete(0,'end')
                roll_no_text.delete(0,'end')
                dept_text.delete(0,'end')
                sem_text.delete(0,'end')

                

        # Save button
        take_image= tk.Button(left_frame,text= "Save",command =Save_Data,font=("times new roman",19,"bold"),bg ="yellow")
        take_image.place(x= 190,y=230,width = 130,height= 50)

        #back function
        def back_b():
                from TkinterDemo import HOME_c
                HOME_c.Home(root)


            # Back
        take_image= tk.Button(left_frame,text= "Back",command = back_b,font=("times new roman",19,"bold"),bg ="yellow")
        take_image.place(x= 340,y=230,width = 130,height= 50)


        root.mainloop()



if __name__ =="__main__":
    root = tk.Tk()
    root.title("AAFR-Automated Attendence System Using Face Recognition")
    root.geometry('1100x600+250+100')
    Student_Data.stud_data(root)
    
    
