from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("stock managment system")
window.geometry("720x640")
my_tree = ttk.Treeview(window, show='headings',height=20)
style=ttk.Style()

placeholderArray = ['','','','','']

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

dummydata = [
    ['12132','weff','fergw','12132','weff','fergw'],
['12132','weff','fergw','12132','weff','fergw'],
['12132','weff','fergw','12132','weff','fergw'],
['12132','weff','fergw','12132','weff','fergw']
]

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in dummydata:
        my_tree.insert(parent='',index='end',iid=array, text="",values=(array),tag="orow")
    my_tree.tag_configure('orow',background="#EEEEEE")
    my_tree.pack()

frame =tkinter.Frame(window, bg = "#02577A")
frame.pack()

btnColor = "#196E78"

manageFrame = tkinter.LabelFrame(frame,text="Manage",borderwidth=5)
manageFrame.grid(row=0, column=0,sticky="w",padx=[10,200],pady=20, ipadx=[6])

saveBtn = Button(manageFrame,text="save",width=10, borderwidth=3,bg=btnColor,fg='white')
updateBtn = Button(manageFrame,text="update",width=10, borderwidth=3,bg=btnColor,fg='white')
deleteBtn = Button(manageFrame,text="delete",width=10, borderwidth=3,bg=btnColor,fg='white')
selectBtn = Button(manageFrame,text="select",width=10, borderwidth=3,bg=btnColor,fg='white')
findBtn = Button(manageFrame,text="find",width=10, borderwidth=3,bg=btnColor,fg='white')
clearBtn = Button(manageFrame,text="clear",width=10, borderwidth=3,bg=btnColor,fg='white')
exportBtn = Button(manageFrame,text="export excel",width=15, borderwidth=3,bg=btnColor,fg='white')

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=5,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)

entriesFrame = tkinter.LabelFrame(frame,text="form",borderwidth=5)
entriesFrame.grid(row=0, column=0,sticky="w",padx=[10,200],pady=[0,20], ipadx=[6])

itemIdlabel= Label(entriesFrame,text= "ITEM ID", anchor="e", width=10)
namelabel= Label(entriesFrame,text= "name", anchor="e", width=10)
pricelabel= Label(entriesFrame,text= "price", anchor="e", width=10)
qntlabel= Label(entriesFrame,text= "qnt", anchor="e", width=10)
categorylabel= Label(entriesFrame,text= "category", anchor="e", width=10)

itemIdlabel.grid(row=0,column=0,padx=10)
namelabel.grid(row=1,column=0,padx=10)
pricelabel.grid(row=2,column=0,padx=10)
qntlabel.grid(row=3,column=0,padx=10)
categorylabel.grid(row=4,column=0,padx=10)

categoryArray = ['networking tools','computer spare parts', 'repair tools','useful gadgets']

itemIdEntry= Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
nameEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[1])
priceEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[2])
qntEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[3])
categoryCombo= ttk.Combobox(entriesFrame,width=47, textvariable=placeholderArray[4],values=categoryArray)

itemIdEntry.grid(row=0,column=0,padx=5, pady= 5)
nameEntry.grid(row=1,column=0,padx=5, pady = 5)
priceEntry.grid(row=2,column=0,padx=5, pady = 5)
qntEntry.grid(row=3,column=0,padx=5, pady= 5)
categoryCombo.grid(row=4,column=0,padx=5, pady =5)

generateIdBtn= Button(entriesFrame,text="genereate id",borderwidth=3,bg=btnColor,fg='white')
generateIdBtn.grid(row=0,column=3,padx=5, pady =5)

style.configure(window)
my_tree['columns']=("Item Id","Name","Price","Quantity","Category","Date")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Item Id", anchor=W,width=70)
my_tree.column("Name", anchor=W,width=100)
my_tree.column("Price", anchor=W,width=100)
my_tree.column("Quantity", anchor=W,width=100)
my_tree.column("Category", anchor=W,width=100)
my_tree.column("Date", anchor=W,width=100)
my_tree.heading("Item Id",text="Irem Id",anchor=W)
my_tree.heading("Name",text="name",anchor=W)
my_tree.heading("Price",text="price",anchor=W)
my_tree.heading("Quantity",text="quantity",anchor=W)
my_tree.heading("Category",text="category",anchor=W)
my_tree.heading("Date",text="date",anchor=W)
my_tree.tag_configure('orow',background="#EEEEEE")
my_tree.pack()

refreshTable()

window.resizable(False, False)
window.mainloop()
