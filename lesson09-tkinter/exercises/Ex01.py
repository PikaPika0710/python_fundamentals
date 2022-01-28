from tkinter import *



def goOn():
    a.set("")
    b.set("")
    rs.set("")

def process():
    x = float(a.get())
    y = float(b.get())
    if x==0 and y ==0:
        z = "Vo so nghiem"
    elif x==0 and y!=0:
        z = "Vo nghiem"
    else:
        z = -y/x;
    rs.set(z)

root = Tk()
a = StringVar()
b = StringVar()
rs = StringVar()
root.title("VietDev")
root.resizable(height=True, width=True)
root.minsize(height=150, width=250)

Label(root, text="Phuong Trinh Bac 1", fg="red", font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)
Label(root, text="He So a: ").grid(row=1, column=0)
Entry(root, width=30, textvariable=a).grid(row=1, column=1)
Label(root, text="He So b: ").grid(row=2, column=0)
Entry(root, width=30, textvariable=b).grid(row=2, column=1)

frameButtom = Frame(root)
Button(frameButtom, text="Giai", command=process).pack(side=LEFT)
Button(frameButtom, text="Tiep", command=goOn).pack(side=LEFT)
Button(frameButtom, text="Thoat", command=root.quit).pack(side=LEFT)
frameButtom.grid(row=3, columnspan=2)

Label(root, text="Ket qua: ").grid(row=4, column=0)
Entry(root, width=30, textvariable=rs).grid(row=4, column=1)
root.mainloop()