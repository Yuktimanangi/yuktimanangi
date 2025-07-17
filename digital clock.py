from tkinter import *
from time import strftime

# Create window
root = Tk()
root.title("Digital Clock")
root.geometry("250x100")
root.configure(bg="black")

# Create label
label = Label(root, font=("Arial", 40), background="black", foreground="cyan")
label.pack(anchor='center')

# Update time function
def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)

time()  # Start clock
root.mainloop()
