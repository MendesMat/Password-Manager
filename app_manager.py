from tkinter import *
from tkinter import messagebox
import pyperclip


class PasswordManagerApp:
    def __init__(self, password_generator):
        self.password_generator = password_generator

        # Window
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # Canvas
        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0)

        # Labels
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1, column=0)

        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=2, column=0)

        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        # Entries
        self.website_input = Entry(width=35)
        self.website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
        self.website_input.focus()

        self.email_input = Entry(width=35)
        self.email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
        self.email_input.insert(0, "mendes.souza.mat@gmail.com")

        self.password_input = Entry(width=21)
        self.password_input.grid(row=3, column=1, sticky="EW")

        # Buttons
        self.password_button = Button(text="Generate Password", command=self.generate_password)
        self.password_button.grid(row=3, column=2, sticky="EW")

        self.add_button = Button(text="Add", width=35, command=self.save_credentials)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

    # Generates a random password for the user
    def generate_password(self):
        generated_password = self.password_generator.generate_password()
        self.password_input.delete(0, END)
        self.password_input.insert(0, generated_password)
        pyperclip.copy(generated_password)

    # Save the credentials inputted from the user
    def save_credentials(self):
        website = self.website_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if website == "" or email == "" or password == "":
            messagebox.showinfo(title="Error", message="Please don't leave fields empty.")
        else:
            is_ok = messagebox.askokcancel(title="Confirm the data", message=f"Website: {website}\n"
                                                                             f"Email: {email}\n"
                                                                             f"Password: {password}\n\n"
                                                                             f"Is it right?")
            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                self.website_input.delete(0, END)
                self.password_input.delete(0, END)

    # Starts the main loop
    def run(self):
        self.window.mainloop()
