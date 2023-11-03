from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PassWord_Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200,highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)
canvas.grid(column=1,row=0)

input_web = Entry(width= 35)
input_web.grid(column=1,row=1,columnspan=2)
input_web.focus()

input_mail = Entry(width= 35)
input_mail.grid(column=1,row=2,columnspan=2)
input_mail.insert(0,"youremail@gmail.com")

input_pass = Entry(width= 21)
input_pass.grid(column=1,row=3)

Website_label = Label(text="Website:", font=("Ariel", 12, "bold"))
Website_label.grid(column=0,row=1)
main_name_label = Label(text="Email/Username:", font=("Ariel", 12, "bold"))
main_name_label.grid(column=0,row=2)
Password_label = Label(text="Password:", font=("Ariel", 12, "bold"))
Password_label.grid(column=0,row=3)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # messagebox.showinfo(title=,message=)
    if input_web.index("end") == 0 or input_pass.index("end")  == 0 :
        messagebox.showinfo(title="Oops",message="Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=input_web,message=f"These are the details entered: \n Email: {input_mail}\n Password:{input_pass}\n is it ok to save?")
        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{input_web.get()} | {input_mail.get()} | {input_pass.get()} \n ")
            input_web.delete(0,END)
            input_pass.delete(0, END)


button_Generate = Button(text="Generate Password",command=generate_password)
button_Generate.grid(column=2,row=3)
button_add = Button(text="Add",width=36,command=save)
button_add.grid(column=1,row=4,columnspan=2)





window.mainloop()