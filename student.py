from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class StudentX:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("2560x1080+0+0")


        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_gender=StringVar()
        self.var_father=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_age=StringVar()
        self.var_radio1=StringVar()




         # yha se photo 1 hai
        try:
            img = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\Screenshot 2024-10-25 210710.png")
            img = img.resize((853, 150), Image.LANCZOS)  # Use LANCZOS for better quality
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=853, height=150)
        except Exception as e:
            print(f"Error loading image: {e}")


            error_msg = Label(self.root, text=f"Error loading image: {e}", fg="red")
            error_msg.pack()

            #yha se photo 2 hai
        try:
            img2 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\Screenshot 2024-10-25 210939.png")
            img2 = img2.resize((853, 150), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl = Label(self.root, image=self.photoimg2)
            f_lbl.place(x=853, y=0, width=853, height=150)
        except Exception as e:
            print(f"Error loading image: {e}")


            error_msg = Label(self.root, text=f"Error loading image: {e}", fg="red")
            error_msg.pack()
          # yha se photo 3 hai
        try:
            img3 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\Screenshot 2024-10-25 210635.png")
            img3 = img3.resize((853, 150), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_lbl = Label(self.root, image=self.photoimg3)
            f_lbl.place(x=1706, y=0, width=853, height=150)
        except Exception as e:
            print(f"Error loading image: {e}")

            error_msg = Label(self.root, text=f"Error loading image: {e}", fg="red")
            error_msg.pack()

            # background photo hai ye
        try:
            img4 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\background 2.jpg")
            img4 = img4.resize((2560, 1080), Image.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=150, width=2560, height=1080)

            title_lbl = Label(bg_img, text=" STUDENT  MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="white", fg="red")
            title_lbl.place(x=0, y=0, width=2560, height=50)

            main_rfame=Frame(bg_img,bd=2)
            main_rfame.place(x=0, y=55, width=2560, height=900)

            # yha se left label table hai
            table_frame = LabelFrame(main_rfame, bd=5,bg="white", relief=RIDGE,text="STUDENT DDETAILS",font=("times new roman",12,"bold"))
            table_frame.place(x=10, y=10, width=1250, height=880)

        
            img_left = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\student.jpg")
            img_left = img_left.resize((853, 150), Image.LANCZOS)  # Use LANCZOS for better quality
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl = Label(main_rfame, image=self.photoimg_left)
            f_lbl.place(x=15, y=30, width=1240, height=150)
                   
                   #CURRENT courese
            current_course_frame = LabelFrame(table_frame, bd=2,bg="white", relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
            current_course_frame.place(x=5, y=155, width=1225, height=200)


               #department
            dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(row=0,column=0,padx=8,sticky=W)

            dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",8,"bold"),state="readonly")
            dep_combo['values'] = ("SELECT DEPTERMANT","IT")
            dep_combo.current(0)
            dep_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

            #course
            course_label=Label(current_course_frame,text="COURSE",font=("times new roman",12,"bold"),bg="white")
            course_label.grid(row=1,column=0,padx=8,sticky=W)

            course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",8,"bold"),state="readonly")
            course_combo['values'] = ("SELECT COURSE","Android Application Development","JAVA","Software Engineering","E-com")
            course_combo.current(0)
            course_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

            #year
            year_label=Label(current_course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
            year_label.grid(row=2,column=0,padx=8,sticky=W)

            year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",8,"bold"),state="readonly")
            year_combo['values'] = ("SELECT YEAR","3rd year")
            year_combo.current(0)
            year_combo.grid(row=2,column=1,padx=3,pady=10,sticky=W)

            #sem
            sem_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",12,"bold"),bg="white")
            sem_label.grid(row=3,column=0,padx=8,sticky=W)

            sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",8,"bold"),state="readonly")
            sem_combo['values'] = ("SELECT SEMESTER","Sem-5")
            sem_combo.current(0)
            sem_combo.grid(row=3,column=1,padx=3,pady=10,sticky=W)


                    #class student information courese
            class_student_frame = LabelFrame(table_frame, bd=2,bg="white", relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
            class_student_frame.place(x=5, y=375, width=1225, height=350)

             #STUDENT NAME
            student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
            student_name_label.grid(row=0,column=0,padx=10,sticky=W)

            student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
            student_name_entry.grid(row=0,column=1,padx=3,pady=10,sticky=W)
            
             #STUDENT ID
            student_id_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
            student_id_label.grid(row=1,column=0,padx=10,sticky=W)

            student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
            student_id_entry.grid(row=1,column=1,padx=3,pady=10,sticky=W)

             #roll no
            roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
            roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

            roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
            roll_no_entry.grid(row=1,column=3,padx=3,pady=10,sticky=W)

             #gender
            gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
            gender_label.grid(row=4,column=0,padx=10,sticky=W)

            gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",8,"bold"),state="readonly")
            gender_combo['values'] = ("SELECT GENDER","Male","Female")
            gender_combo.current(0)
            gender_combo.grid(row=4,column=1,padx=3,pady=10,sticky=W)

            #father name
            FatherName_label=Label(class_student_frame,text="Father Name:",font=("times new roman",12,"bold"),bg="white")
            FatherName_label.grid(row=0,column=2,padx=10,sticky=W)

            FatherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_father,width=20,font=("times new roman",12,"bold"))
            FatherName_entry.grid(row=0,column=3,padx=3,pady=10,sticky=W)

            #email
            email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
            email_label.grid(row=2,column=2,padx=10,sticky=W)

            email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
            email_entry.grid(row=2,column=3,padx=3,pady=10,sticky=W)

            #phone no
            phone_no_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
            phone_no_label.grid(row=3,column=0,padx=10,sticky=W)

            phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
            phone_no_entry.grid(row=3,column=1,padx=3,pady=10,sticky=W)

            #address
            address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
            address_label.grid(row=4,column=2,padx=10,sticky=W)

            address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
            address_entry.grid(row=4,column=3,padx=3,pady=10,sticky=W)

            #teacher name
            teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
            teacher_name_label.grid(row=3,column=2,padx=10,sticky=W)

            teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
            teacher_name_entry.grid(row=3,column=3,padx=3,pady=10,sticky=W)

            #age
            age_label=Label(class_student_frame,text="Age:",font=("times new roman",12,"bold"),bg="white")
            age_label.grid(row=2,column=0,padx=10,sticky=W)

            age_entry=ttk.Entry(class_student_frame,textvariable=self.var_age,width=20,font=("times new roman",12,"bold"))
            age_entry.grid(row=2,column=1,padx=3,pady=10,sticky=W)

            #radio button
            self.var_radio1=StringVar()
            radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo smple",value="yes")
            radiobtn1.grid(row=0,column=4,padx=10,sticky=W)

            radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="photo smple",value="no")
            radiobtn2.grid(row=0,column=5,padx=10,sticky=W)

            #button frame
            btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame.place(x=5, y=230, width=1200, height=40)

            save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=24,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            save_btn.grid(row=0, column=0, padx=4, pady=0)

            update_btn=Button(btn_frame,text="UPDATE",width=24,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            update_btn.grid(row=0, column=1, padx=4, pady=0)

            delete_btn=Button(btn_frame,text="DELETE",width=24,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            delete_btn.grid(row=0, column=2, padx=4, pady=0)

            reset_btn=Button(btn_frame,text="RESET",width=24,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            reset_btn.grid(row=0, column=3, padx=4, pady=0)

            #button frame
            btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame1.place(x=5, y=280, width=1200, height=40)

            take_photo_btn=Button(btn_frame1,text="TAKE PHOTO SAMPLE",width=50,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            take_photo_btn.grid(row=0, column=0, padx=4, pady=0)

            UPDATE_PHOTO_btn=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",width=50,height=1,font=("times new roman",15,"bold"),bg="skyblue",fg="black")
            UPDATE_PHOTO_btn.grid(row=0, column=1, padx=4, pady=0)



             # yha se right label table hai
            table_rightframe = LabelFrame(main_rfame, bd=5,bg="white", relief=RIDGE,text="STUDENT DDETAILS",font=("times new roman",12,"bold"))
            table_rightframe.place(x=1270, y=10, width=1250, height=880)


            img_right = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\face a.jpg")
            img_right = img_right.resize((853, 150), Image.LANCZOS)  # Use LANCZOS for better quality
            self.photoimg_right = ImageTk.PhotoImage(img_right)

            f_lbl = Label(table_rightframe, image=self.photoimg_right)
            f_lbl.place(x=0, y=0, width=1240, height=150)


        # =========search system==========
            search_frame = LabelFrame(table_rightframe, bd=2,bg="white", relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
            search_frame.place(x=5, y=155, width=1225, height=72)

            search_bar_label=Label(search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="white",fg="navy blue")
            search_bar_label.grid(row=0,column=0,padx=10,sticky=W)

            search_combo=ttk.Combobox(search_frame,font=("times new roman",8,"bold"),state="readonly")
            search_combo['values'] = ("SELECT SEMESTER","ROLL NO","PHONE NO","NAME")
            search_combo.current(0)
            search_combo.grid(row=0,column=1,padx=15,pady=10,sticky=W)

            search_entry=ttk.Entry(search_frame,width=22,font=("times new roman",12,"bold"))
            search_entry.grid(row=0,column=2,padx=15,pady=10,sticky=W)


            search_btn=Button(search_frame,text="SEARCH",width=20,height=1,font=("times new roman",10,"bold"),bg="skyblue",fg="black")
            search_btn.grid(row=0, column=3,padx=15,pady=0)

            showALL_btn=Button(search_frame,text="SHOW ALL",width=20,height=1,font=("times new roman",10,"bold"),bg="skyblue",fg="black")
            showALL_btn.grid(row=0, column=4,padx=15,pady=0)

            # ==============table frame=================
            table_frame = Frame(table_rightframe, bd=2,bg="white", relief=RIDGE)
            table_frame.place(x=5, y=245, width=1225, height=300)

            scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

            self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","student_name","student_id","roll_no","gender","father_name","email","phone_no","address","teacher_name","age","radio"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)

            self.student_table.heading("dep",text="Departement")
            self.student_table.heading("course",text="Course")
            self.student_table.heading("year",text="Year")
            self.student_table.heading("sem",text="Semester")
            self.student_table.heading("student_name",text="Student Name")
            self.student_table.heading("student_id",text="Student ID")
            self.student_table.heading("roll_no",text="Roll No")
            self.student_table.heading("gender",text="Gender")
            self.student_table.heading("father_name",text="Father's Name")
            self.student_table.heading("email",text="Email")
            self.student_table.heading("phone_no",text="Phone No")
            self.student_table.heading("address",text="Address")
            self.student_table.heading("teacher_name",text="Teacher Name")
            self.student_table.heading("age",text="Age")
            self.student_table.heading("radio",text="Select")
            self.student_table["show"] = "headings"
            #set width
            self.student_table.column("dep", width=100)
            self.student_table.column("course", width=100)
            self.student_table.column("year", width=100)
            self.student_table.column("sem", width=100)
            self.student_table.column("student_name", width=150)
            self.student_table.column("student_id", width=100)
            self.student_table.column("roll_no", width=100)
            self.student_table.column("gender", width=100)
            self.student_table.column("father_name", width=150)
            self.student_table.column("email", width=150)
            self.student_table.column("phone_no", width=150)
            self.student_table.column("address", width=200)
            self.student_table.column("teacher_name", width=150)
            self.student_table.column("age", width=100)
            self.student_table.column("radio", width=100)

            self.student_table.pack(fill=BOTH, expand=1)

        except Exception as e:
            print(f"Error loading image: {e}")
            error_msg = Label(self.root, text=f"Error loading image: {e}", fg="red")
            error_msg.pack()


    def add_data(self):   
          if self.var_dep.get()=="Select Departement" or self.var_name.get()=="" or self.var_id.get()=="":
                        messagebox.showerror("Error","All Fields Are Required",parent=self.root)
          else:
                         config = {
                          'host':'localhost',
                          'user':'root',
                          'password':'admin@23',
                          'database':'face_recognizer'
      
                    }
          try:
                          connection = mysql.connector.connect(**config)
                          if connection.is_connected(): 
                                print("Connect to the database")
          except mysql.connector.connect_error as err:
                          print(f"Error: {err}")
          finally:
                        if connection.is_connected():
                          connection.close()
                          print("MySQL connection is closed")
                          
                        try:
                    # conn=mysql.connector.connect(host="localhost",username="root",password="admin@123",database="face_recognizer")
                            my_cursor=connection.cursor()
                            my_cursor.execute("INSERT INTO student (dep, course, year, sem, student name, student_id, Roll_no, Gender, Father_Name, E-mail, Phone_No, Address, Teacher_Name, Age, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                                                                        self.var_id.get(),
                                                                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                                                                        self.var_father.get(),
                                                                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                                                                        self.var_age.get(),
                                                                                                                                                                                                                                                                                        self.var_radio1.get()

                                                                                                                                                                                                                                                                                     ))
                            # my_cursor.fetchall()
                            # connection.commit()
                            # connection.close()
                            messagebox.showinfo("Success","Data Inserted Successfully",parent=self.root)
                        except Exception as es:
                            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



            
if __name__ == "__main__":
        root = Tk()
        obj = StudentX(root)
        root.mainloop()
