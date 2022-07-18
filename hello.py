from developer import Developer
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from face_recongnition import Face_Recognisation
from photos import Photos
from exit import Exit
from attendence import Attendence

class Face_Recognisation_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\facialrecognition.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # C:\Users\IMRAN_YOUNAS\OneDrive - SSUET\Desktop\Pthton_project_Ai\img
        # img1 = Image.open(r"C:\Users\IMRAN_YOUNAS\OneDrive - SSUET\Desktop\Pthton_project_Ai\img\images.jpg")
        # img1 = img1.resize((500,130),Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # f_lbl = Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=0,y=0,width=500,height=130)

        #   2nd img
        img2 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\facialrecognition.png")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # 3rd image
        img3 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\university.jpg")
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=400,height=130)
         # bg img
        img4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\di.jpg")
        img4 = img4.resize((1500,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=710)

        ttl_lbl = Label(bg_img,text="Face Recognition System",font=("times new roman",35,"bold"),bg="white",fg="red")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)
        # Student btn
        img4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\student.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.phtobtn1 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.phtobtn1,command=self.student_details,cursor="hand2")  #bg image k andar btn bnana hai islye
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Detail",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        b1_1.place(x=200,y=300,width=220,height=40)  
        # detect_face btn

        img_btn2 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\face_detector1.jpg")
        img_btn2 = img_btn2.resize((220,220),Image.ANTIALIAS)
        self.phtobtn2 = ImageTk.PhotoImage(img_btn2)

        btn1 = Button(bg_img,image=self.phtobtn2,command=self.face_data,cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=500,y=100,width=220,height=220)

        btn1 = Button(bg_img,text="Face detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=500,y=300,width=220,height=40)

        #  Attendence btn

        img_btn3 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\smart-attendance.jpg")
        img_btn3 = img_btn3.resize((220,220),Image.ANTIALIAS)
        self.phtobtn3 = ImageTk.PhotoImage(img_btn3)

        btn1 = Button(bg_img,image=self.phtobtn3,command=self.Att_data, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=800,y=100,width=220,height=220)

        btn1 = Button(bg_img,text="Attendence ",command=self.Att_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=800,y=300,width=220,height=40)
        
        #  Photos donr btn
        
        img_btn4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\std4.jpg")
        img_btn4 = img_btn4.resize((220,220),Image.ANTIALIAS)
        self.phtobtn4 = ImageTk.PhotoImage(img_btn4)

        btn1 = Button(bg_img,image=self.phtobtn4,command=self.photo_data, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=1100,y=100,width=220,height=220)

        btn1 = Button(bg_img,text="Photos",command=self.photo_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=1100,y=300,width=220,height=40)

        
        #  Attendence btn
        
        img_btn5 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\help.jpg")
        img_btn5 = img_btn5.resize((220,220),Image.ANTIALIAS)
        self.phtobtn5 = ImageTk.PhotoImage(img_btn5)

        btn1 = Button(bg_img,image=self.phtobtn5, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=200,y=350,width=220,height=220)

        btn1 = Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=200,y=520,width=220,height=40)
        
        #  photos btn
        img_btn6 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\help.jpg")
        img_btn6 = img_btn5.resize((220,220),Image.ANTIALIAS)
        self.phtobtn6 = ImageTk.PhotoImage(img_btn6)

        btn1 = Button(bg_img,image=self.phtobtn6, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=500,y=350,width=220,height=220)

        btn1 = Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=500,y=520,width=220,height=40)
        
        # img_btn6 = Image.open(r"C:\Users\IMRAN_YOUNAS\OneDrive - SSUET\Desktop\Pthton_project_Ai\img\help.jpg")
        # img_btn6 = img_btn6.resize((220,220),Image.ANTIALIAS)
        # self.phtobtn6 = ImageTk.PhotoImage(img_btn6)

        # btn1 = Button(bg_img,image=self.phtobtn6, cursor="hand2")   #bg image k andar btn bnana hai islye
        # btn1.place(x=500,y=350,width=220,height=220)

        # btn1 = Button(bg_img,text="PhotoS", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        # btn1.place(x=500,y=520,width=220,height=40)
        
         #  developer btn
        
        img_btn7 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\dev.jpg")
        img_btn7 = img_btn7.resize((220,220),Image.ANTIALIAS)
        self.phtobtn7 = ImageTk.PhotoImage(img_btn7)

        btn1 = Button(bg_img,image=self.phtobtn7,command=self.dev_data, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=800,y=350,width=220,height=220)

        btn1 = Button(bg_img,text="Developer",command=self.dev_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=800,y=520,width=220,height=40)

          #  exit btn
        
        img_btn8 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\exit.jpg")
        img_btn8 = img_btn8.resize((220,220),Image.ANTIALIAS)
        self.phtobtn8 = ImageTk.PhotoImage(img_btn8)

        btn1 = Button(bg_img,image=self.phtobtn8,command=self.exit_data, cursor="hand2")   #bg image k andar btn bnana hai islye
        btn1.place(x=1100,y=350,width=220,height=220)

        btn1 = Button(bg_img,text="Exit", command=self.exit_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")   #bg image k andar btn bnana hai islye
        btn1.place(x=1100,y=520,width=220,height=40)

    def student_details(self):
      self.new_window  = Toplevel(self.root)
      self.app = Student(self.new_window)
    def face_data(self):
      self.new_window  = Toplevel(self.root)
      self.app = Face_Recognisation(self.new_window) 
    def photo_data(self):
      self.new_window  = Toplevel(self.root)
      self.app = Photos(self.new_window) 
    def dev_data(self):
      self.new_window  = Toplevel(self.root)
      self.app = Developer(self.new_window) 
    def exit_data(self):
      self.new_window  = Toplevel(self.root)
      self.app = Exit(self.new_window) 
    def Att_data(self):
      self.new_window  = Toplevel(self.root)
      self.app = Attendence(self.new_window) 
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognisation_System(root)
    root.mainloop()