from tkinter import *

root = Tk()
root.title("VietDev")
root.resizable(height=True, width=True)
root.minsize(height = 200, width=300)

Label(root, text="Hello world", fg = "red").pack()
Button(root, text="Click Me", command=root.quit).pack()
e=StringVar()
Entry(root, textvariable=e, width=30).pack()
e.set("Tran Cong Viet")

root.mainloop()