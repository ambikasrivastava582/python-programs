from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------------- Main Window ----------------
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# ----------- Image -----------
try:
    upload = Image.open("im.png")   # Keep image in same folder
    upload = upload.resize((300, 250))
    image = ImageTk.PhotoImage(upload)
    img_label = Label(root, image=image, bg='light blue')
    img_label.place(x=180, y=20)
except:
    Label(root, text="Image not found", bg="light blue").place(x=260, y=120)

# ----------- Welcome Text -----------
label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue', font=("Arial", 11, "bold"))
label1.place(relx=0.5, y=320, anchor=CENTER)


# ---------------- Function to open Top Window ----------------
def msg():
    messagebox.showinfo("Alert", "Let’s calculate the denomination count!")
    topwin()


def topwin():
    global entry, t1, t2, t3

    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('400x350')

    Label(top, text="Enter Amount", bg="grey",
          font=("Arial", 12, "bold")).pack(pady=10)

    entry = Entry(top, font=("Arial", 12))
    entry.pack()

    Button(top, text="Calculate", command=calculator,
           bg="brown", fg="white").pack(pady=10)

    Label(top, text="₹2000 Notes", bg="grey").pack()
    t1 = Entry(top)
    t1.pack()

    Label(top, text="₹500 Notes", bg="grey").pack()
    t2 = Entry(top)
    t2.pack()

    Label(top, text="₹100 Notes", bg="grey").pack()
    t3 = Entry(top)
    t3.pack()


# ---------------- Calculator ----------------
def calculator():
    try:
        amount = int(entry.get())

        note2000 = amount // 2000
        amount %= 2000

        note500 = amount // 500
        amount %= 500

        note100 = amount // 100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, note2000)
        t2.insert(END, note500)
        t3.insert(END, note100)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


# ----------- Start Button -----------
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white',
    font=("Arial", 11, "bold"))
button1.place(x=260, y=350)

root.mainloop()