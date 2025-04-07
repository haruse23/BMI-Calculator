from customtkinter import *
from tkinter import *
def BMI():
    weight = float(entry1.get())
    height = float(entry2.get())
    BMI = weight / height ** 2

    if BMI < 18.5:
        label3.configure(text="You're underweight")
        label4.configure(text=f"{format(BMI,'.1f')}")

    elif BMI <= 24.9 and BMI >= 18.5:
        label3.configure(text="You're normal")
        label4.configure(text=f"{format(BMI,'.1f')}")

    elif BMI >= 25 and BMI <= 29.9:
        label3.configure(text="You're overweight")
        label4.configure(text=f"{format(BMI,'.1f')}")
        
    else:
        label3.configure(text="You're obese")
        label4.configure(text=f"{format(BMI,'.1f')}")




set_appearance_mode('DARK')

window = CTk()

window.geometry("800x640")
window.title("BMI")


label1 = CTkLabel(window, text="Weight (Kg): ", font=("Georgia", 30, "bold"), text_color='#70a862')
label1.pack()
label1.place(relx=0.1, rely=0.25)

label2 = CTkLabel(window, text="Height (m): ", font=("Georgia", 30, "bold"), text_color='#75acd9')
label2.pack()
label2.place(relx=0.65, rely=0.25)


entry1 = CTkEntry(window, text_color='black', bg_color="black", fg_color="white", font=("Georgia", 20), placeholder_text="Enter..",placeholder_text_color='#70a862')
entry1.pack()
entry1.configure(width=200,height=40)
entry1.place(relx=0.1, rely=0.37)



entry2 = CTkEntry(window, text_color='black', bg_color="black", fg_color="white", font=("Georgia", 20),placeholder_text="Enter..",placeholder_text_color='#75acd9')
entry2.pack()
entry2.configure(width=200,height=40)
entry2.place(relx=0.645, rely=0.3675)


button = CTkButton(window, text="Calculate BMI", command=BMI, font=('Arial', 20), anchor=CENTER,border_width=3, border_color='black')
button.pack()
button.configure(width=300,height=100)
button.place(relx=0.31 ,rely=0.55)


label3 = CTkLabel(window,justify='center',text="",text_color='white', font=("Georgia", 30, "bold"), bg_color='#8ca2ad', anchor=CENTER,corner_radius=16)
label3.pack()
label3.configure(width=450,height=50)
label3.place(relx=0.215, rely=0.78)


label4 = CTkLabel(window,justify='center',text="",text_color='white', font=("Georgia", 30, "bold"), bg_color='#8ca2ad', anchor=CENTER,corner_radius=16)
label4.pack()
label4.configure(width=100,height=40)
label4.place(relx=0.431, rely=0.1)


window.mainloop()



















