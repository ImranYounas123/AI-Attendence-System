from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class Photos:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("FAce Recognition System")

        ttl_lbl = Label(self.root,text="Photoes Captured ",font=("times new roman",35,"bold"),bg="darkgrey",fg="darkgreen")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)
        f_lbl.grid(pady=4)
        img2 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img2 = img2.resize((200,200,),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=200,width=200,height=200)
        f_lbl.grid(pady=4)


        img3 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img3 = img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=200,y=0,width=200,height=200)
        f_lbl.grid(pady=5)

        img4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img4 = img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_lbl = Label(self.root,image=self.photoimg4)
        f_lbl.place(x=400,y=0,width=200,height=200)
        f_lbl.grid(pady=5)
        img1 = Image.open(r"C:\Users\IMRAN_YOUNAS\OneDrive - SSUET\Desktop\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)


        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)

        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\imran.jpeg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=200)




if __name__ == "__main__":
    root=Tk()
    obj=Photos(root)
    root.mainloop()