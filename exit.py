from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class Exit:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")

        ttl_lbl = Label(self.root,text="Feedback   Thankyou :) ",font=("times new roman",35,"bold"),bg="darkgrey",fg="darkgreen")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)

        #img
        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\BestFacialRecognition.jpg")
        img1 = img1.resize((1400,700),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=1400,height=700)





if __name__ == "__main__":
    root=Tk()
    obj=Exit(root)
    root.mainloop()