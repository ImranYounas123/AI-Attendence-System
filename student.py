from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("FAce Recognition System")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_std_name = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



         #   first imag
        img1 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\std2.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #   2nd img
        img2 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\img\std3.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # 3rd image
        img3 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\img\std4.jpg")
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)
    #   bg img 
        img4 = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\img\di.jpg")
        img4 = img4.resize((1500,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=710)

        ttl_lbl = Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        ttl_lbl.place(x=0,y=0,width=1500,height=45)

        #frame for student management System..
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10,y=55,width=1400,height=600)

        #label frmes mai hum title de sakty hai 
        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) #main_frame islye q k isky andar bnana hai label 
        left_frame.place(x=10,y=10,width=660,height=580)
        # img left 
        img_left = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\smart-attendance.jpg")
        img_left = img2.resize((620,130),Image.ANTIALIAS)
        self.photoimg2_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame,image=self.photoimg2_left)
        f_lbl.place(x=5,y=0,width=620,height=130)
#========================================================================================================================
        #current Course Information ........................
        current_Course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current Course Information",font=("times new roman",12,"bold")) #main_frame islye q k isky andar bnana hai label 
        current_Course_frame.place(x=5,y=135,width=616,height=150) #img k neechy toh y = 130 q k height 130 hai 
        #labelsssss...............
        # 1 . department Combobox
        depart_label = Label(current_Course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        depart_label.grid(row=0,column=0,padx=10,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni

        depart_combo = ttk.Combobox(current_Course_frame,textvariable = self.var_dep, font=("times new roman",12,"bold"),state="readonly")  #yeh cmbo box ttk k ander aata hai
        depart_combo["values"] = ("select Department","Computer","SE","IT","CS")
        depart_combo.current(0) # 0 curent yaani phali select deparatment
        depart_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # 2 . Course Combobox
        depart_label = Label(current_Course_frame,text="Courses",font=("times new roman",12,"bold"),bg="white")
        depart_label.grid(row=0,column=2,padx=10 ,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni

        depart_combo = ttk.Combobox(current_Course_frame,textvariable = self.var_course,font=("times new roman",12,"bold"),state="readonly")  #yeh cmbo box ttk k ander aata hai
        depart_combo["values"] = ("select Course","Artificial Intelligent","Software Construction & Development","E_Commerce","Human Computer & Interction","Computer Communication & Networking")
        depart_combo.current(0) # 0 curent yaani phali select deparatment
        depart_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)  # sickyy agr scell bra ho 

        # 3 . Year Combobox
        depart_label = Label(current_Course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
        depart_label.grid(row=1,column=0,padx=10,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni

        depart_combo = ttk.Combobox(current_Course_frame,textvariable = self.var_year,font=("times new roman",12,"bold"),state="readonly")  #yeh cmbo box ttk k ander aata hai
        depart_combo["values"] = ("select Year", "2019-20","2020-21","2021-22","2022-23","2023-24")
        depart_combo.current(0) # 0 curent yaani phali select deparatment
        depart_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # 4. Semester Combobox
        depart_label = Label(current_Course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        depart_label.grid(row=1,column=2,padx=10,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni

        depart_combo = ttk.Combobox(current_Course_frame,textvariable = self.var_semester,font=("times new roman",12,"bold"),state="readonly")  #yeh cmbo box ttk k ander aata hai
        depart_combo["values"] = ("select Semester","1st-Semester","2nd-Semester","3rd-Semester","4th-Semester","5th-Semester")
        depart_combo.current(0) # 0 curent yaani phali select deparatment
        depart_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
#=======================================================================================================================
        #Class Student Information ........................
        Class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold")) #main_frame islye q k isky andar bnana hai label 
        Class_Student_frame.place(x=0,y=240,width=620,height=300) #img k neechy toh y = 130 q k height 130 hai 
        # 1. Student_ID label======================================================================
        Student_ID_label = Label(Class_Student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        Student_ID_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable = self.var_std_id,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=0,column=1,padx=5,pady=2,sticky=W)   

        # 2. Student_Name label======================================================================
        Student_Name_label = Label(Class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=0,column=3,padx=5,pady=2,sticky=W)

        # 3. Student_didivision label======================================================================
        Student_didivision_label = Label(Class_Student_frame,text="Student didivision",font=("times new roman",12,"bold"),bg="white")
        Student_didivision_label.grid(row=1,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=1,column=1,padx=5,pady=2,sticky=W)

        # 4. Student_Roll_no label======================================================================
        Student_Roll_no_label = Label(Class_Student_frame,text="Student Roll-No",font=("times new roman",12,"bold"),bg="white")
        Student_Roll_no_label.grid(row=1,column=2,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=1,column=3,padx=5,pady=2,sticky=W)

        # 5. Gender label======================================================================
        Student_Gender_label = Label(Class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Student_Gender_label.grid(row=2,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        # 6.Email label======================================================================
        Student_Email_label = Label(Class_Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        Student_Email_label.grid(row=2,column=2,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=2,column=3,padx=5,pady=2,sticky=W)
        
        # 7. phone_no label======================================================================
        Student_phone_no_label = Label(Class_Student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        Student_phone_no_label.grid(row=3,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=3,column=1,padx=5,pady=2,sticky=W)
        
        # 8. Address_No label======================================================================
        Student_Address_No_label = Label(Class_Student_frame,text="Address No",font=("times new roman",12,"bold"),bg="white")
        Student_Address_No_label.grid(row=3,column=2,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=3,column=3,padx=5,pady=2,sticky=W)
        
        # 9. Teacher_Name label======================================================================
        Student_Teacher_Name_label = Label(Class_Student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Student_Teacher_Name_label.grid(row=4,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        #Entry Fields ------
        StudentEntry = ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        StudentEntry.grid(row=4,column=1,padx=5,pady=2,sticky=W)
        
        # Radio Buttons============================
        self.var_radio =StringVar()
        Radiobutton1 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="Take photo sample", value="Yes")
        Radiobutton1.grid(row=5,column=0)

        Radiobutton2 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="No photo sample", value="Yes")
        Radiobutton2.grid(row=5,column=1)
        # btn frames
        btn_frame = Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=615,height=45)
        # save btn 
        Save_DB_BTN = Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Save_DB_BTN.grid(row=0,column=0,padx=1)
        # update btn 
        update_DB_BTN = Button(btn_frame,text="update",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_DB_BTN.grid(row=0,column=1,padx=1)
        # delete btn 
        delete_DB_BTN = Button(btn_frame,text="delete",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_DB_BTN.grid(row=0,column=2,padx=1)
        # reset btn 
        reset_DB_BTN = Button(btn_frame,text="reset",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_DB_BTN.grid(row=0,column=3,padx=1)

        take_DB_BTN = Button(btn_frame,text="Take Photo",width=10,font=("times new roman",12,"bold"),bg="red",fg="white")
        take_DB_BTN.grid(row=0,column=4,padx=1)
        update_DB_BTN = Button(btn_frame,text="Uodate Photo",width=10,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_DB_BTN.grid(row=0,column=5,padx=1)

        # table Frame==============================================================



        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) #main_frame islye q k isky andar bnana hai label 
        Right_frame.place(x=680,y=10,width=660,height=580)
        # img right 
        img_right = Image.open(r"E:\Study\5th semester\SWE_214 (Artificial Intelligent)\Python_Projects\Pthton_project_Ai\img\std1.jpg")
        img_right = img2.resize((620,130),Image.ANTIALIAS)
        self.photoimg2_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image=self.photoimg2_right)
        f_lbl.place(x=5,y=0,width=650,height=130)

        # ***********************Search System***********************************
          #Search Frame ........................
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold")) #main_frame islye q k isky andar bnana hai label 
        Search_frame.place(x=5,y=150,width=640,height=100) #img k neechy toh y = 130 q k height 130 hai 
        # Search Label 
        Search_label = Label(Search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="grey",fg="white")
        Search_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)     #grid mai rows or columns hoty hai agr kahi le k jana hai to grid ko le k jaa skty hai row column ko ni
        # Search Combobox 
        Search_combo = ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly")  #yeh cmbo box ttk k ander aata hai
        Search_combo["values"] = ("select","Roll_NO","Phone_NO")
        Search_combo.current(0) # 0 curent yaani phali select deparatment
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  # sickyy agr scell bra h
        
        
        # Entert Field 
        Search_Entry = ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_Entry.grid(row=0,column=2,padx=5,pady=2,sticky=W)   
        
        # btn ____________________________
         # update btn 
        Search_BTN = Button(Search_frame,text="Search",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_BTN.grid(row=0,column=3,padx=2)
        # delete btn 
        ShowAll_BTN = Button(Search_frame,text="Show ALL",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_BTN.grid(row=0,column=4,padx=2)
        
          #table Frame ........................
        table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE) #main_frame islye q k isky andar bnana hai label 
        table_frame.place(x=5,y=250,width=640,height=230) #img k neechy toh y = 130 q k height 130 hai

        #Scroll Bar =====
        Scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_tbl = ttk.Treeview(table_frame,column=("dep","Course","year","Sem","Id","Name","Roll_no","Gender","div","dob","E-mail","Phone","Address","Teacher","Photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command = self.student_tbl.xview)
        Scroll_y.config(command = self.student_tbl.yview)

        self.student_tbl.heading("dep",text="Department")
        self.student_tbl.heading("Course",text="Courses")
        self.student_tbl.heading("year",text="Year")
        self.student_tbl.heading("Sem",text="Semester")
        self.student_tbl.heading("Id",text="Student ID")
        self.student_tbl.heading("Name",text="Name")
        self.student_tbl.heading("Roll_no",text="Roll No")
        self.student_tbl.heading("Gender",text="Gender")
        self.student_tbl.heading("div",text="Division")
        self.student_tbl.heading("dob",text="DOB")
        self.student_tbl.heading("E-mail",text="E-Mail")
        self.student_tbl.heading("Phone",text="Phone")
        self.student_tbl.heading("Address",text="Address")
        self.student_tbl.heading("Teacher",text="Teacher")
        self.student_tbl.heading("Photo",text="PhotoSampleStatus")
        self.student_tbl["show"]="headings"
        # ===========width Setting
        self.student_tbl.column("dep",width=100)
        self.student_tbl.column("Course",width=100)
        self.student_tbl.column("year",width=100)
        self.student_tbl.column("Sem",width=100)
        self.student_tbl.column("Id",width=100)
        self.student_tbl.column("Name",width=100)
        self.student_tbl.column("Roll_no",width=100)
        self.student_tbl.column("Gender",width=100)
        self.student_tbl.column("div",width=100)
        self.student_tbl.column("dob",width=100)
        self.student_tbl.column("E-mail",width=100)
        self.student_tbl.column("Phone",width=100)
        self.student_tbl.column("Address",width=100)
        self.student_tbl.column("Teacher",width=100)
        self.student_tbl.column("Photo",width=100)
        self.student_tbl.pack(fill=BOTH,expand=1)

    def add_data(self):
          if self.var_dep.get()=="Select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
          else:
                pass
        




    
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()