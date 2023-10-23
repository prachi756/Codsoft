import tkinter as tk
import random
import string

def generate_password():
    length = int(password_length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(chars) for _ in range(length))
    generated_password_label.config(text=generated_password)

def accept_password():
    accepted_passwords_list.insert(tk.END, generated_password_label.cget("text"))

def reset_password():
    password_length_entry.delete(0, tk.END)
    generated_password_label.config(text="")

screen = tk.Tk()
screen.title("Password Generator")

input_frame = tk.Frame(screen, bg="lightblue")
input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

generate_frame = tk.Frame(screen, bg="lightgreen")
generate_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

display_frame = tk.Frame(screen, bg="lightyellow")
display_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

accept_frame = tk.Frame(screen, bg="lightcoral")
accept_frame.grid(row=3, column=0, padx=10, pady=10)

reset_frame = tk.Frame(screen, bg="lightgray")
reset_frame.grid(row=3, column=1, padx=10, pady=10)

input_label = tk.Label(input_frame, text="Password Length:")
input_label.grid(row=0, column=0)
password_length_entry = tk.Entry(input_frame)
password_length_entry.grid(row=0, column=1)

generate_button = tk.Button(generate_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=0, columnspan=2)

generated_password_label = tk.Label(display_frame, text="")
generated_password_label.grid(row=0, column=0, columnspan=2)

accept_button = tk.Button(accept_frame, text="Accept", command=accept_password)
accept_button.grid(row=0, column=0)

reset_button = tk.Button(reset_frame, text="Reset", command=reset_password)
reset_button.grid(row=0, column=0)

accepted_passwords_list = tk.Listbox(screen)
accepted_passwords_list.grid(row=4, columnspan=2, padx=10, pady=10)

screen.mainloop()