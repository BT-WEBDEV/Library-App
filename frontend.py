############# BOOKSTORE APP #################
"""
Case Use - The BookStore App stores the following boook information: 
Title, Author, Year, ISBN

The User Can:
View All Books
Search For A Book
Add Books
Update Book Information
Delete Books
Close The Program
"""

# from the tkinter library we will import all classes along with backend script
from tkinter import *
import backend

#### Frontend Wrapper Functions ####

#function GET SELECTED ROW lets user select a row from the listbox
#global variable SELECTED TUPLE 
def get_selected_row(event): 
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    #input book information into entry fields when selected from list
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

#function VIEW ALL command button - delete clears the list box first then shows the database contents
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

#function SEARCH ENTRY command button - clear list, then get method from user inputs. 
def search_command(): 
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

#function ADD COMMAND button - inputs new book info, clears list, and displays the added book into list
def add_command(): 
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    #insert - 2nd parameter is all in one to display as a line in list, rather than seperate values
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

#function DELETE COMMAND button - deletes a selected tuple (row) from database and list
def delete_command():
    backend.delete(selected_tuple[0])

#function UPDATE COMMAND button - once selected, you can update book information from the entry fields
#update paraments - keep the ID (0 index) the same, but get the updated information from the entry fields. 
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


### GUI ###
# window variable is the window of the program itself. 
window=Tk()
window.wm_title("Library App")

#Form Labels for Book Data
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#Inputs for Book Data - StringVar takes the string and turns it into a variable.
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#List Box - This will contain our list of books with addtional information in a string
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_row)

#Scroll Bar for the List of Books
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#Configure scrollbar to the list. 
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Buttons
b1=Button(window,text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window,text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window,text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window,text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

# mainloop keeps the programming functioning until closed by user.
window.mainloop()
