from tkinter import *
import os
#window for register
def register():
    global reg_screen
    reg_screen = Toplevel(fs)
    reg_screen.title("REGISTER")
    reg_screen.geometry("300x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(reg_screen, text="PLEASE ENTER THE BELOW DETAILS TO REGISTER", bg="skyblue").pack()
    Label(reg_screen, text="").pack()
    L1 = Label(reg_screen, text="USERNAME")
    L1.pack()
    username_entry = Entry(reg_screen, textvariable=username)
    username_entry.pack()
    L2 = Label(reg_screen, text="PASSWORD")
    L2.pack()
    password_entry = Entry(reg_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(reg_screen, text="").pack()
    Button(reg_screen, text="SUBMIT", width=15, height=1, bg="skyblue", command=register_user).pack()

#window for login

def login():
    global login_screen
    login_screen = Toplevel(fs)
    login_screen.title("LOGIN")
    login_screen.geometry("300x300")
    Label(login_screen, text="ENTER THE LOGIN DETAILS",bg ='skyblue',font = 20).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    L1 = Label(login_screen, text="USERNAME").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    L2 = Label(login_screen, text="PASSWORD").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="LOGIN", width=10, height=1,bg='skyblue',command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(reg_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():

    import main
    main.get_response("HI")


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("250x200")
    Label(password_not_recog_screen, text="INVALID PASSWORD ").pack()
    Button(password_not_recog_screen, text="EXIT", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("300x300")
    Label(user_not_found_screen, text="USER NOT FOUND").pack()
    Button(user_not_found_screen, text="EXIT", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def first_screen():
    global fs
    fs = Tk()
    fs.geometry("350x280")
    fs.title("CHATBOT LOGIN")
    Label(text="SELECT YOUR CHOICE", bg="skyblue", width="250", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="LOGIN", height="2", width="40", command=login).pack()
    Label(text="").pack()
    Button(text="REGISTER", height="2", width="40", command=register).pack()
    fs.mainloop()


first_screen()

