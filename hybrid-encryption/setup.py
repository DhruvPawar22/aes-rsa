from tkinter import *
from tkinter import ttk
from Cryptography.hybrid_encryption import *
from getpass import getuser
from tkinter.filedialog import askopenfilename
from ttkthemes import themed_tk as tk


def message(name, button, mgs_label):

    button['state'] = DISABLED 
    if button["text"] == "Encryption":
        mgs = encryption(name)
        mgs_label.config(text=mgs)

    if button["text"] == "Decryption":
        mgs = decryption(name)
        mgs_label.config(text=mgs)


def open_file():
    
    username = getuser()
    initialdirectory = "C:/Users/{}".format(username)
    name = askopenfilename(initialdir=initialdirectory,
                           filetypes=[("All Files", "*.*")],
                           title="Choose a file you want to encrypt/decrypt"
                           )
    if name:
        file_name = get_file_name(name, extension=True)
        label.config(text=file_name)
        separator2 = ttk.Separator(root, orient='horizontal')
        separator2.place(relx=0, rely=0.38, relwidth=1, relheight=1)
        mgs_label = ttk.Label(root)
        mgs_label.place(x=0, y=150)
        encrypt_button = ttk.Button(root, text="Encryption", command=lambda: message(name, encrypt_button, mgs_label))
        decrypt_button = ttk.Button(root, text="Decryption", command=lambda: message(name, decrypt_button, mgs_label))
        encrypt_button.place(x=90, y=80)
        decrypt_button.place(x=310, y=80)


root = tk.ThemedTk()
root.get_themes()
root.set_theme("clearlooks")
icon = PhotoImage(file="images/icon.png")  
root.iconphoto(False, icon)
app_width = 500  
app_height = 200  
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))
root.geometry(f"{app_width}x{app_height}+{x}+{y}")
root.resizable(0, 0)  
title = root.title("AES+RSA Hybrid-Encryption, Dhruv Pawar-215891050")
title_label = ttk.Label(root, text=" AES+RSA Hybrid File Encryption ", font=("Arial", 16))
title_label.pack()
separator1 = ttk.Separator(root, orient='horizontal')
separator1.place(relx=0, rely=0.20, relwidth=1, relheight=1)
chose_file_button = ttk.Button(root, text="Select File", command=open_file).pack()
label = ttk.Label(root, text="Add file") 
label.pack()

root.mainloop()
