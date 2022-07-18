from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class Face_Recognisation:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("FAce Recognition System")

        ttl_lbl = Label(self.root,text="Face Rconition ",font=("times new roman",35,"bold"),bg="darkgrey",fg="darkgreen")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)

        #img
        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\face_detector1.jpg")
        img1 = img1.resize((650,700),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=650,height=700)

        img4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img4 = img4.resize((950,700),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=650,y=45,width=950,height=650)

        #btn
        b1_1 = Button(bg_img,text="Face recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="darkred",fg="white")   #bg image k andar btn bnana hai islye
        b1_1.place(x=380,y=590,width=200,height=40)  










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognisation(root)
    root.mainloop()