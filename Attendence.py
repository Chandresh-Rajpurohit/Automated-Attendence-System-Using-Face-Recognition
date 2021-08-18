import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
import numpy
import csv
import os
from tkinter import filedialog,messagebox

class Record:

    def Att_record(r):

        root = r
            

        image2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\face.jpeg')
        image2 = image2.resize((1100,600),Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        label1 = tk.Label(image = image1)
        label1.place(x=0,y=0,width= 1100,height= 600)


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
        text_bg= tk.Label(text ="Attendence  Record",font=("times new roman",28,"bold"),bg= "orange",fg= "purple",bd = 12)
        text_bg.place(x=0,y=80,width=1100,height= 40)

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


        main_Frame = tk.Frame()
        main_Frame.place(x=0,y=120,width= 1100,height= 400)



        #Background img
        image2 =Image.open('E:\\CHANDRESH\\python\\AAFR\\images\\face.jpeg')
        image2 = image2.resize((1100,500),Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)
        label1 = tk.Label(main_Frame,image = image1)
        label1.place(x=0,y=0,width= 1100,height= 500)


        left_frame = tk.LabelFrame(main_Frame,bd =4, text = "Student Details", font=("times new roman",15,"bold"),fg= "red")
        left_frame.place(x= 30,y= 20,width= 690,height= 360)


        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11))
        

        scroll_y= ttk.Scrollbar(left_frame,orient=tk.VERTICAL)
        Stu_table = ttk.Treeview(left_frame,column = ("Roll No","Name","Department","Semester","Attendence"),yscrollcommand= scroll_y.set,height= 15)
        scroll_y.pack(side=tk.RIGHT,fill = tk.Y)
        Stu_table.heading("Roll No",text = "Roll No")
        Stu_table.heading("Name",text = "Name")
        Stu_table.heading("Department",text = "Department")
        Stu_table.heading("Semester",text = "Semester")
        Stu_table.heading("Attendence",text = "Attendence")
        Stu_table["show"] ="headings"
        Stu_table.column("Roll No",width= 130,anchor="center")
        Stu_table.column("Name",width= 130,anchor="center")
        Stu_table.column("Department",width= 130,anchor="center")
        Stu_table.column("Semester",width= 130,anchor="center")
        Stu_table.column("Attendence",width= 130,anchor="center")

        df = pd.read_csv("E:\\CHANDRESH\\python\\AAFR\\Attendence\\Attendence_Record.csv",header=None)
        
        df_rows= df.to_numpy().tolist()
        for row in df_rows:
            Stu_table.insert("","end",values= row)
                        
        Stu_table.pack()  

        #save Atendence function
        def Save_Att():
                fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title= "Open CSV",filetypes =(("CSV File","*.csv"),("All File","*.*")),parent =root)
                with open(fln,mode= "w",newline= "") as myfile:
                        exp =csv.writer(myfile,delimiter=",") 
                        for row_id in Stu_table.get_children():
                                row = Stu_table.item(row_id)['values']
                                exp.writerow(row)
                        messagebox.showinfo("Data Exported","Your Data has saved")
                        

        #Save Attendence button
        Bt1 = tk.Button(text = "Save Attendence",command = Save_Att,font=("times new roman",19,"bold"),fg= "black",bg = "orange")
        Bt1.place(x= 800,y= 200,width =250,height = 50)


        #clear record functiom
        def clear_record():

            fileVariable = open("E:\\CHANDRESH\\python\\AAFR\\Attendence\\Attendence_Record.csv", 'r+')
            fileVariable.truncate(0)
            fileVariable. close()

            for i in Stu_table.get_children():
                Stu_table.delete(i)

            
        #Reset Button
        Bt2 = tk.Button(text = "Reset",command = clear_record,font=("times new roman",19,"bold"),fg= "black",bg = "orange")
        Bt2.place(x= 800,y= 290,width =250,height = 50)

        #back functon
        def Back():
            from TkinterDemo import HOME_c
            HOME_c.Home(root)
    
        #back button
        Bt3 = tk.Button(text = "Back",command = Back,font=("times new roman",19,"bold"),fg= "black",bg = "orange")
        Bt3.place(x= 800,y= 380,width =250,height = 50)
            
        
        root.mainloop()



if __name__ =="__main__":
    root = tk.Tk()
    root.title("AAFR-Automated Attendence System Using Face Recognition")
    root.geometry('1100x600+250+100')
    Record.Att_record(root)






