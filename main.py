import vigenere
import tkinter as tk
from tkinter import ttk

def SHOW_E_TEXT_(): #SHOW ENCRYPTED TEXT BETWEEN ENTRIES AND BUTTON
    e_text["text"]=vigenere.ENCRYPT_(e_key.get(), p_text.get())
def SHOW_D_TEXT_(): #SHOW DECRYPTED TEXT BETWEEN ENTRIES AND BUTTON
    d_text["text"]=vigenere.DECRYPT_(d_key.get(), enc_text.get())
app=tk.Tk()
app.title("Vigenère Encryptor and Decryptor")


#ENCRYPTION PART
e_key=ttk.Entry(app)
p_text=ttk.Entry(app)
e_text=ttk.Label(app, anchor=tk.W)
e_button=ttk.Button(app, command=SHOW_E_TEXT_, text="ENCRYPT")
e_key.grid()
p_text.grid()
e_text.grid()
e_button.grid()

#DECRYPTION PART
d_key=ttk.Entry(app)
enc_text=ttk.Entry(app)
d_text=ttk.Label(app)
d_button=ttk.Button(app, command=SHOW_D_TEXT_, text="DECRYPT")
d_key.grid(row=0,column=2)
enc_text.grid(row=1,column=2)
d_text.grid(row=2,column=2)
d_button.grid(row=3,column=2)

#FANCY PART
key_text=tk.Label(app, text="KEY")
dec_or_enc_text=tk.Label(app, text="PLAINTEXT | ENCRYPTED TEXT")
enc_or_dec_text=tk.Label(app, text="ENCRYPTED TEXT | PLAINTEXT")
key_text.grid(row=0, column=1)
dec_or_enc_text.grid(row=1,column=1)
enc_or_dec_text.grid(row=2, column=1)
app.mainloop()