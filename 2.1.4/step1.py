#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    if(ent_username.get() == "username" and ent_password.get() == "pass"):
        frame_auth.tkraise()
    else:
        lbl_fail = tk.Label(frame_login, text="VICINITY OF OBSCENITY IN YOUR EYES!!")
        lbl_fail2 = tk.Label(frame_login, text="Terracotta pie, hey")
        lbl_fail3 = tk.Label(frame_login, text="Terracotta pie, hey")
        lbl_fail4 = tk.Label(frame_login, text="Terracotta pie, hey")
        lbl_fail5 = tk.Label(frame_login, text="Terracotta pie")
        lbl_fail6 = tk.Label(frame_login, text="BANANA BANANA BANANA BANANA TERRACOTTA")
        lbl_fail7 = tk.Label(frame_login, text="BANANA TERRACOTTA!! TERRACOTTA PIE!")
        lbl_fail8 = tk.Label(frame_login, text="BANANA BANANA BANANA BANANA TERRACOTTA")
        lbl_fail9 = tk.Label(frame_login, text="BANANA TERRACOTTA!! TERRACOTTA PIE!")
        lbl_fail.pack()
        lbl_fail2.pack()
        lbl_fail3.pack()
        lbl_fail4.pack()
        lbl_fail5.pack()
        lbl_fail6.pack()
        lbl_fail7.pack()
        lbl_fail8.pack()
        lbl_fail9.pack()
# main window
root = tk.Tk()
root.wm_geometry("300x400")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=5)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:',font="Courier")
lbl_password.pack()

ent_password = tk.Entry(frame_login, show='*', bd=5)
ent_password.pack(pady=10, padx=80)

lbl_login = tk.Label(frame_login, text='Log In', font="Courier")
lbl_login.pack()

btn_login = tk.Button(frame_login, bd=5, command= test_my_button)
btn_login.pack()



frame_login.tkraise()
root.mainloop()