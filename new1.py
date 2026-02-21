from tkinter import *
from tkinter import messagebox

# -------- Main Window --------
root = Tk()
root.title("Denomination Counter")
root.geometry("500x300")
root.configure(bg="light blue")

Label(root,
      text="Welcome to Denomination Counter",
      font=("Arial", 14, "bold"),
      bg="light blue").pack(pady=20)

# -------- Function to open Top Window --------
def open_counter():
    global entry, t1, t2, t3

    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.geometry("400x300")
    top.configure(bg="light grey")

    Label(top, text="Enter Amount",
          font=("Arial", 12, "bold"),
          bg="light grey").pack(pady=10)

    entry = Entry(top, font=("Arial", 12))
    entry.pack()

    Button(top, text="Calculate",
           command=calculate,
           bg="brown", fg="white").pack(pady=10)

    Label(top, text="₹2000 Notes", bg="light grey").pack()
    t1 = Entry(top)
    t1.pack()

    Label(top, text="₹500 Notes", bg="light grey").pack()
    t2 = Entry(top)
    t2.pack()

    Label(top, text="₹100 Notes", bg="light grey").pack()
    t3 = Entry(top)
    t3.pack()

# -------- Calculator --------
def calculate():
    try:
        amount = int(entry.get())

        n2000 = amount // 2000
        amount %= 2000

        n500 = amount // 500
        amount %= 500

        n100 = amount // 100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, n2000)
        t2.insert(END, n500)
        t3.insert(END, n100)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# -------- Button --------
Button(root,
       text="Start Denomination Counter",
       command=open_counter,
       bg="brown",
       fg="white",
       font=("Arial", 11, "bold")).pack(pady=20)

root.mainloop()