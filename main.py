from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import StudentX

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("2560x1080+0+0")
        
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
            img4 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\background.jpg")
            img4 = img4.resize((2560, 1080), Image.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=150, width=2560, height=1080)

            title_lbl = Label(bg_img, text="FACE   RECOGNITION   ATTENDANCE   SYSTEM", font=("times new roman", 40, "bold"), bg="white", fg="red")
            title_lbl.place(x=0, y=0, width=2560, height=50)

        except Exception as e:
            print(f"Error loading image: {e}")
            error_msg = Label(self.root, text=f"Error loading image: {e}", fg="red")
            error_msg.pack()

# STUDENT BUTTON
        try:
           img5 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\student.jpg")
           img5 = img5.resize((240, 240), Image.LANCZOS)
           self.photoimg5 = ImageTk.PhotoImage(img5)

           b1 = Button(bg_img, image=self.photoimg5,command=self.student_details,cursor="hand2")
           b1.place(x=400, y=100, width=240, height=200)

           b1_text = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=400, y=290, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()




           # capture button
        try:
           img6 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\fce de.jpg")
           img6 = img6.resize((240, 240), Image.LANCZOS)
           self.photoimg6 = ImageTk.PhotoImage(img6)

           b1 = Button(bg_img, image=self.photoimg6,cursor="hand2")
           b1.place(x=800, y=100, width=240, height=200)

           b1_text = Button(bg_img,text=" FACE DETETOR",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=800, y=290, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()



              # attendance ka button
        try:
           img7 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\attenndance.jpg")
           img7 = img7.resize((240, 240), Image.LANCZOS)
           self.photoimg7 = ImageTk.PhotoImage(img7)

           b1 = Button(bg_img, image=self.photoimg7,cursor="hand2")
           b1.place(x=1200, y=100, width=240, height=200)

           b1_text = Button(bg_img,text=" ATTENDANCE ",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=1200, y=290, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()


              # help button
        try:
           img8 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\help.jpg")
           img8 = img8.resize((240, 240), Image.LANCZOS)
           self.photoimg8 = ImageTk.PhotoImage(img8)

           b1 = Button(bg_img, image=self.photoimg8,cursor="hand2")
           b1.place(x=1600, y=100, width=240, height=200)

           b1_text = Button(bg_img,text="  HELP  ",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=1600, y=290, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()


                 # train button
        try:
           img9 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\data an.jpg")
           img9 = img9.resize((240, 240), Image.LANCZOS)
           self.photoimg9 = ImageTk.PhotoImage(img9)

           b1 = Button(bg_img, image=self.photoimg9,cursor="hand2")
           b1.place(x=400, y=400, width=240, height=200)

           b1_text = Button(bg_img,text="DATA UPDATE",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=400, y=590, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()

            # photos button
        try:
           img10 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\photo 1.jpg")
           img10 = img10.resize((240, 240), Image.LANCZOS)
           self.photoimg10 = ImageTk.PhotoImage(img10)

           b1 = Button(bg_img, image=self.photoimg10,cursor="hand2")
           b1.place(x=800, y=400, width=240, height=200)

           b1_text = Button(bg_img,text="PHOTOS",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=800, y=590, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()

              # developer button
        try:
           img11 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\information.jpg")
           img11 = img11.resize((240, 240), Image.LANCZOS)
           self.photoimg11 = ImageTk.PhotoImage(img11)

           b1 = Button(bg_img, image=self.photoimg11,cursor="hand2")
           b1.place(x=1200, y=400, width=240, height=200)

           b1_text = Button(bg_img,text="DEVELOPER",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=1200, y=590, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()


               # exit button
        try:
           img12 = Image.open(r"C:\Users\KRISHNA\Desktop\Face Recognition System\isme sarri photo hai\exit.jpg")
           img12 = img12.resize((240, 240), Image.LANCZOS)
           self.photoimg12 = ImageTk.PhotoImage(img12)

           b1 = Button(bg_img, image=self.photoimg12,cursor="hand2")
           b1.place(x=1600, y=400, width=240, height=200)

           b1_text = Button(bg_img,text="EXIT",cursor="hand2" ,font=("times new roman",19, "bold"), bg="white", fg="blue")
           b1_text.place(x=1600, y=590, width=240, height=45)


        except Exception as e:
           print(f"Error loading student button image: {e}")
           error_msg = Label(self.root, text=f"Error loading student button image: {e}", fg="red")
           error_msg.pack()
    def student_details(self):
         self.new_window = Toplevel(self.root)
         self.app = StudentX(self.new_window)

         
          

           




          


    




if __name__ == "__main__":
      root = Tk()
      obj = Face_Recognition_System(root)
      root.mainloop()