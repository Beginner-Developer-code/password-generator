import string
import random
import tkinter as tk
from tkinter import ttk
import os

def generate_password():
    characters = []
    requirements = {}


    if checkbox_uppercase_value.get() == '1':
        characters.extend(string.ascii_uppercase)
        requirements['upper'] = False
    if checkbox_lowercase_value.get() == '1':
        characters.extend(string.ascii_lowercase)
        requirements['lower'] = False
    if checkbox_digits_value.get() == '1':
        characters.extend(string.digits)
        requirements['digits'] = False
    if checkbox_puntuaction_value.get() == '1':
        characters.extend(string.punctuation)
        requirements['punctuation'] = False

    if int(entry_length.get()) >= 4:
        password = ''.join(random.choice(characters) for _ in range(int(entry_length.get())))

        while True:

            if checkbox_uppercase_value.get() == '1':
                requirements['upper'] = False
            if checkbox_lowercase_value.get() == '1':
                requirements['lower'] = False
            if checkbox_digits_value.get() == '1':
                requirements['digits'] = False
            if checkbox_puntuaction_value.get() == '1':
                requirements['punctuation'] = False

            for i in password:
                if i in string.ascii_uppercase:
                    requirements['upper'] = True
                if i in string.ascii_lowercase:
                    requirements['lower'] = True
                if i in string.digits:
                    requirements['digits'] = True
                if i in string.punctuation:
                    requirements['punctuation'] = True

            if all(requirements.values()):
                break
            else:
                password = ''.join(random.choice(characters) for _ in range(int(entry_length.get())))

        

        result.config(state='normal')
        result.delete(0,tk.END)
        result.insert(0, f"Password: {password}")
        result.config(state='readonly')
    else:
        result.config(state='normal')
        result.delete(0,tk.END)
        result.insert(0, f"La password deve essere di minimo 4 caratteri!!")
        result.config(state='readonly')

def check(value,text):
    if value.get() == '1':
        text.set("Selezionato")
    else:
        text.set("Non selezionato")

def check_button():
    
    value = entry_length.get()

    if value == "" or (checkbox_uppercase_value.get() != '1' and checkbox_lowercase_value.get() != '1' and checkbox_digits_value.get() != '1' and checkbox_puntuaction_value.get() != '1'):
        button.config(state="disabled")
    else:
        try:
            isinstance(int(value), int)
        except ValueError:
            print("ValueError")
        finally:
            button.config(state="normal")

    window.after(100, check_button)

window = tk.Tk()
window.title("Password generator")
window.geometry("1024x900")
window.resizable(False, False)

title = ttk.Label(window, text="Password generator", font=('Impact',40,'bold')).pack(pady=20)
label_options = ttk.Label(window, text="Imposta le seguenti opzioni: ", font=("Courier New", 15), foreground="red").pack()

#Length
label_length = ttk.Label(window, text="Inserisci la lunghezza della password ", font=("Courier New", 12)).pack(pady=30)
entry_length = ttk.Entry(window, width=30, justify='center', font=("Courier New", 9))
entry_length.pack()

#Upper
checkbox_uppercase_value = tk.StringVar()
checkbox_uppercase_text = tk.StringVar()
checkbox_uppercase_text.set("Non selezionato")
label_uppercase = ttk.Label(window, text="Lettere maiuscole ", font=("Courier New", 12)).pack(pady=30)
checkbox_uppercase = ttk.Checkbutton(window, textvariable=checkbox_uppercase_text ,variable=checkbox_uppercase_value ,onvalue=1, offvalue=0, command=lambda: check(checkbox_uppercase_value,checkbox_uppercase_text)).pack()

#Lower
checkbox_lowercase_value = tk.StringVar()
checkbox_lowercase_text = tk.StringVar()
checkbox_lowercase_text.set("Non selezionato")
label_lowercase = ttk.Label(window, text="Lettere minuscole ", font=("Courier New", 12)).pack(pady=30)
checkbox_lowercase = ttk.Checkbutton(window, textvariable=checkbox_lowercase_text ,variable=checkbox_lowercase_value ,onvalue=1, offvalue=0, command=lambda: check(checkbox_lowercase_value,checkbox_lowercase_text)).pack()

#Digits
checkbox_digits_value = tk.StringVar()
checkbox_digits_text = tk.StringVar()
checkbox_digits_text.set("Non selezionato")
label_digits = ttk.Label(window, text="Numeri ", font=("Courier New", 12)).pack(pady=30)
checkbox_digits = ttk.Checkbutton(window, textvariable=checkbox_digits_text ,variable=checkbox_digits_value ,onvalue=1, offvalue=0, command=lambda: check(checkbox_digits_value,checkbox_digits_text)).pack()

#Puntuaction
checkbox_puntuaction_value = tk.StringVar()
checkbox_puntuaction_text = tk.StringVar()
checkbox_puntuaction_text.set("Non selezionato")
label_puntuaction = ttk.Label(window, text="Simboli speciali ", font=("Courier New", 12)).pack(pady=30)
checkbox_puntuaction = ttk.Checkbutton(window, textvariable=checkbox_puntuaction_text ,variable=checkbox_puntuaction_value ,onvalue=1, offvalue=0, command=lambda: check(checkbox_puntuaction_value,checkbox_puntuaction_text)).pack()

style = ttk.Style()
style.configure('TButton', font=('Courier New',12))
button = ttk.Button(window, text="Genera password", style="TButton", state="disabled", command=generate_password)
button.pack(pady=35)

#Events
window.after(100, check_button)

result = ttk.Entry(window,state="readonly",width=80, justify="center", font=("Helvetica", 15 ,'bold'))
result.pack(pady=25, ipady=50)

window.mainloop()

