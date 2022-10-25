from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if website == "" or username == "" or password == "":
        messagebox.showinfo(message="Dejaste datos vacios")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Data:\nusername: {username},\nPassword:{password}")
        if is_ok:
            with open("passwords.txt",  "a") as f:
                f.write(f"{website} | {username} | {password}|\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website: ")
username_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")
generate_password_btn = Button(text="Generate Password")
website_entry = Entry(width=45)
username_entry = Entry(width=45)
password_entry = Entry(width=26)
email = StringVar()
add_btn = Button(text="Add", width=42, command=save_data)

username_entry.insert(0, "alejandro-perry2011@hotmail.com")
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_password_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
