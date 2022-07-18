from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\developer.jpeg")
        img1 = img1.resize((650,700),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=650,height=700)

        ttl_lbl = Label(self.root,text="Team Members ",font=("times new roman",35,"bold"),bg="darkgrey",fg="darkgreen")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)

        ttl_lbl = Label(self.root,text="1    :Imran Younas ",font=("times new roman",35,"bold"),fg="darkred")
        ttl_lbl.place(x=200,y=100,width=1550,height=45)
        ttl_lbl = Label(self.root,text=" 2    :Furqan Farooqui ",font=("times new roman",35,"bold"),fg="darkred")
        ttl_lbl.place(x=220,y=150,width=1550,height=45)
        ttl_lbl = Label(self.root,text=" 3    :  Osama  ",font=("times new roman",35,"bold"),fg="darkred")
        ttl_lbl.place(x=133,y=200,width=1550,height=45)
        ttl_lbl = Label(self.root,text=" 3    :  Noor  ",font=("times new roman",35,"bold"),fg="darkred")
        ttl_lbl.place(x=120,y=250,width=1550,height=45)

        img2 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\developer.jpeg")
        img2 = img2.resize((650,700),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=650,height=700)

        img3 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\di.jpg")
        img3 = img3.resize((800,500),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=651,y=300,width=800,height=500)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()