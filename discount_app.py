import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from currencies import Currency


class GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Options for dropdown menu
        options = [
            "BGN",
            "EUR",
            "USD",
            "GBP",
            "AED",
            "RUB",
            "JPY"
        ]
        global clicked
        # Datatype of menu text
        clicked = tk.StringVar()
        # Initial menu text
        clicked.set("Currency")

        # Create dropdown menu
        self.dropdown_menu = tk.OptionMenu(self, clicked, *options)
        self.dropdown_menu.config(font=Font(family=('Arial', 12)), width=15, anchor='center')
        self.dropdown_menu.pack(fill='both')

        # Sum
        self.sum_label = tk.Label(text=f"Sum", font=('Arial', 15), bg='cyan', anchor='center')
        self.number_entry = tk.Entry(font=16)
        self.sum_label.pack(padx=10, pady=10, fill='both')
        self.number_entry.pack(padx=10)

        # Discount
        self.discount_label = tk.Label(text="Discount (%)", font=('Arial', 15), bg='cyan', anchor='center')
        self.discount_entry = tk.Entry(font=16)
        self.discount_label.pack(padx=10, pady=10, fill='both')
        self.discount_entry.pack(padx=10)

        # Button
        self.calculate_button = tk.Button(text="Total Sum", font=('Arial', 12), command=self.calculate_discount)
        self.calculate_button.pack(padx=10, pady=10)

        # Output
        self.output = tk.Label(padx=10, bg='cyan')
        self.output.pack()

    # Calculations
    def calculate_discount(self):
        try:
            currency_sign = Currency(clicked.get())
            entry_sum = self.number_entry.get()
            entry_percentage = self.discount_entry.get()
            errors = []
            if entry_sum == "":
                errors.append("SUM AREA EMPTY!")
            if entry_percentage == "":
                errors.append("DISCOUNT AREA EMPTY!")

            if errors:
                new_line = '\n'
                if len(errors) == 1:
                    messagebox.showerror(title="Error!", message="Error: " + errors[0])
                else:
                    messagebox.showerror(title="Error!", message=f"Errors: {new_line.join(errors)}")

            if float(entry_sum) < 0:
                self.output.config(text="POSITIVE NUMBERS ONLY!", bg="red", fg="black")
            elif float(entry_percentage) < 0:
                self.output.config(text="POSITIVE NUMBERS ONLY!", bg="red", fg="black")
            else:
                discount_sum = float(entry_percentage) / 100 * float(entry_sum)
                final_price = float(entry_sum) - float(discount_sum)
                self.output.config(text=currency_sign.get_money_format(f"{final_price:.2f}"), font=('Arial', 15), bg="green", fg="white")
        except (Exception, ValueError):
            self.output.config(text="CURRENCY NOT SELECTED!", bg="red", fg="black")


app = GUI()
app.master.title('Discount Calculator')
# app.master.maxsize(500, 275) # Lock the window maximize option
app.master.minsize(500, 275)    # Lock the window minimize option
app.master.geometry('+500+275')  # LOck the window position
app.master.configure(bg='cyan')
app.master.iconbitmap(r'E:\Desktop\Programming\Python\discount-calculator\calculator.ico')  # Change the directory

app.mainloop()
