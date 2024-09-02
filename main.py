'''
THE PROGRAM CURRENTLY REMAINS UNCOMPLTETED. -9th August, 2024
'''

#IMPORTS
from tkinter import *
from tkinter import ttk
import csv      #   FOR SAVING DATE #AFTER SWITCHING TO PANDAS, I HONESTLY DON'T REMEMBER WHAT THIS IS FOR, BUT IT DOESN'T HURT TO KEEP THIS...
import pandas as pd
from tkinter import messagebox

#data_file = "D:/ALL PYTHON CODES/Python Projects Folder/PROJECT FILES/data.txt"
#CLASS
class Borrowedbook:     #   CLASS TO CREATE DATA

    global bookName
    global bookID
    global bookAuthor
    global cardID



    def __init__(self, book_Name, book_ID, book_Author, card_ID, Status):
        self.name = book_Name
        self.bookId = book_ID
        self.author = book_Author
        self.status = Status
        self.borrowerId = card_ID


        global table
        # WHEN CLASS INSTANTIATED, TREE VIEW DISPLAY DATA
        table.insert(parent='', index=0, values=(self.name, self.author, self.bookId, self.borrowerId, self.status))
        #print(self.name, self.author, self.bookId, self.borrowerId)


"""     FUNCTIONS   """

def Submit_Button_Pressed():
    # GET DATA IN ENTRY FIELD
    bookName = Book_name.get()
    bookID = Book_ID.get()
    bookAuthor = Author.get()
    cardID = Card_ID.get()

        # CHECK IF CHECKBOX IS TICKED
    global issued_checked_var
    global issued_status
    if issued_checked_var.get() == 1:
        issued_status = 'Issued'
    elif issued_checked_var.get() == 0:
        issued_status = 'Returned'
    # INSTANTIATE CLASS
    Borrowedbook(bookName, bookID, bookAuthor, cardID, issued_status)
    # CLEAR ENTRY FIELDS


    # GO TO SPECIFIED ENTRY FIELD
    Book_name.focus()
    #   SAVE DATA
    new_row = {'bookName':[bookName], 'bookID':[bookID], 'bookAuthor':[bookAuthor], 'CardID':[cardID], 'issued_status':[issued_status]}
    new_row_dataframe = pd.DataFrame(new_row)
    to_bottom = pd.read_csv(csv_loc)
    actual = new_row_dataframe._append(to_bottom, ignore_index=True, sort=False)
    actual.to_csv(csv_loc, mode='w', index=False)   #, header=False





# GO TO THE VIEW WINDOW - switches addrecord frame to the viewrecord frame. searches can be performed here.
def view_button_pressed():
    new_record_frame.pack_forget()
    view_record_frame.pack(fill=BOTH, expand=1)

# GO TO THE ASS RECORD WINDOW - switches to the add record frame
def back_to_home():
    view_record_frame.pack_forget()
    new_record_frame.pack(fill=BOTH, expand=1)
    show_all()

# SEARCH FEATURE
def search(): #pretty delf explanatory
    for record in table.get_children():
        table.delete(record)
    fetch = searched.get()
    int(fetch)
    '''
        csv_open = open(csv_loc)
    csv_read = csv.reader(csv_open)
    csv_list = list(csv_read)
    '''
    pd_csv = pd.read_csv(csv_loc)

    eol_count = 0   #end of loop count

    for row in range(0, rowNum):
        print(f"row={row}, rowNum={rowNum}")
        if pd_csv.loc[row, 'cardID'] == fetch:
            table.insert(parent='', index=END, values=(pd_csv.loc[row, 'bookName'], pd_csv.loc[row, 'bookAuthor'], pd_csv.loc[row, 'bookID'], pd_csv.loc[row, 'cardID'], pd_csv.loc[row, 'issued_status']))
            eol_count += 1
        if (row == rowNum-1)&(eol_count == 0):
            messagebox.showinfo("Search Results", "No result")
    print(eol_count)




# DELETE SELECTED RECORDS
def delete_records():#deleted selected records
    if table.selection():
        del_or_not = messagebox.askyesno("Warning!", "Are you sure you want to delete?")
        if del_or_not==True:
            x = table.selection() # GET ALL SELECTED ROWS

            del_pd_csv = pd.read_csv(csv_loc)

            for df_to_d in x:
                del_pd_csv.drop(index=table.index(df_to_d), inplace=True)

            for to_d in x:
                table.delete(to_d) # DELETE SELECTION

            del_pd_csv.to_csv(csv_loc, mode='w', index=False)   #, header=False

            messagebox.showinfo("Deleted", "Data deleted.")
        elif (del_or_not==False):
            messagebox.showinfo("Process Cancelled", "Selected records not deleted.")

    else:
        messagebox.showinfo("No selection made", 'Please select records to delete.')






# SELECT ALL RECORDS
def select_all_records(): #again self explanatory
    if is_checked.get() == 1:
        to_s = table.get_children() # GET ALL ROWS
        table.selection_set(to_s) # SELECT ALL ROWS
    elif is_checked.get() == 0:
        to_s = table.get_children() # GET ALL ROWS
        table.selection_remove(to_s) # DESELECT ALL ROWS

def Delete_Entry(): # delete data in entry boxes for the add record frame
    Book_name.delete(0, END)
    Book_ID.delete(0, END)
    Author.delete(0, END)
    Card_ID.delete(0, END)
    Issued_Checkbox.deselect()

"""     CREATING GUI    """

# WINDOW PROPERTIES
win = Tk()
win.title("LIBRARY RECORDS")
win.geometry("1200x600")


# CREATING FRAMES
top_frame = Frame(win, bg="#006699")
main_left_frame = Frame(win)        # HOLDS THE 'NEW RECORDS FRAME' AND THE 'VIEW FRAME'
new_record_frame = Frame(main_left_frame, bg="#66CCFF")
view_record_frame = Frame(main_left_frame, bg='black')
right_frame = Frame(win, bg="black")        # HOLDS ALL FRAMES A THE RIGHT SIDE OF THE WINDOW
frame1 = Frame(right_frame, bg="#00AAFF")
frame2 = Frame(right_frame, bg="white")
mid_row = Frame(right_frame, bg="#0077b3")
buttons_frame = Frame(main_left_frame, bg="Yellow")     # HOLDS ALL BUTTONS ON TOP OF 'MAIN_LEFT_FRAME'


# TOP LABELS
Label(win, text="LIBRARY MANAGEMENT SYSTEM", fg="white", bg="#006699", font=('Calibri', 15, 'bold')).pack(fill=X, ipady=10)
Label(mid_row, text="INFORMATION ABOUT ALL BOOKS", bg="#0077b3").pack(ipady=10)


#       NEW RECORDS FRAME WIDGETS
Label(new_record_frame, text="Book Name", bg="#66CCFF").pack(pady=(30, 0))
Book_name = Entry(new_record_frame)
Book_name.pack()
Label(new_record_frame, text="Book ID", bg="#66CCFF").pack(pady=(30, 0))
Book_ID = Entry(new_record_frame)
Book_ID.pack()
Label(new_record_frame, text="Author(s)", bg="#66CCFF").pack(pady=(30, 0))
Author = Entry(new_record_frame)
Author.pack()
Label(new_record_frame, text="Issuer's Card ID", bg="#66CCFF").pack(pady=(30, 0))
Card_ID = Entry(new_record_frame)
Card_ID.pack()
Label(new_record_frame, text="Status", bg="#66CCFF").pack(pady=(30, 0))
issued_checked_var = IntVar()
Issued_Checkbox = (Checkbutton(new_record_frame, text="Issued", bg="#66CCFF", variable=issued_checked_var))
Issued_Checkbox.pack()
Accept_input = Button(new_record_frame, text="Add new record", bg="#3366FF", command=Submit_Button_Pressed).pack(ipadx=20, pady=10)
Clear_Fields = Button(new_record_frame, text="Clear Fields", bg="#3366FF", command=Delete_Entry).pack(ipadx=20, pady=10)

#       VIEW RECORDS FRAME WIDGET
Label(view_record_frame, text="Search", fg='white', bg='black').pack(pady=(30, 0))
global searched
searched = Entry(view_record_frame)
searched.pack()
search_button = Button(view_record_frame, text="Search", command=search).pack(pady=(10, 0))


#       TREEVIEW TABLE
table = ttk.Treeview(frame2, columns=('BookName', 'Author', 'BookID', 'CardId', 'Status'), show='headings') #, 'Status'
table.column('Status',  width=10)
table.column('BookID',  width=20)
table.column('CardId',  width=20)
table.heading('BookName', text="BOOK NAME")
table.heading('Author', text="AUTHOR")
table.heading('BookID', text="BOOK ID")
table.heading('CardId', text="CARD ID")
table.heading('Status', text="STATUS")
table.pack(fill=BOTH, expand=1)


#       BUTTONS FOR BUTTONS FRAME
Button(buttons_frame, text="Add New Record", bg="#3366FF", command=back_to_home).pack(side=LEFT)
Button(buttons_frame, text="View record", bg="#3366FF", command=view_button_pressed).pack(side=LEFT)
Button(buttons_frame, text="Delete record", bg="#3366FF", command=delete_records).pack(side=LEFT)
is_checked = IntVar()
Checkbutton(buttons_frame, text="Select All", bg="#00AAFF", variable=is_checked, command=select_all_records).pack(side=LEFT, fill=BOTH)


#       TO FIND THE VARIOUS FRAMES
"""Label(buttons_frame, text="buttons frame").pack(pady=20, padx=20)
Label(main_left_frame, text="main left frame").pack(pady=20, padx=20)
Label(right_frame, text="right frame").pack(pady=20, padx=20)
Label(frame1, text="frame1").pack(pady=20, padx=20)
Label(mid_row, text="mid_row").pack(pady=20, padx=20)
Label(frame2, text="frame2").pack(pady=20, padx=20)
"""

#       PACKING ALL FRAMES
buttons_frame.pack(side=TOP, anchor='w')
main_left_frame.pack(fill=Y, side=LEFT)
new_record_frame.pack(fill=BOTH, expand=1)
right_frame.pack(fill=BOTH, expand=1, side=RIGHT)
mid_row.pack(fill=X)
frame2.pack(fill=BOTH, expand=1)


#   SHOWING ALREADY PRESENT DATA
global csv_loc
csv_loc = "PROJECT FILES/data.csv"
def show_all():
    csv_open = pd.read_csv(csv_loc)
    global rowNum
    rowNum = csv_open.shape[0]

    for i in range(0, rowNum):
        table.insert(parent='', index=END, values=(csv_open.loc[i, 'bookName'], csv_open.loc[i, 'bookAuthor'], csv_open.loc[i, 'bookID'], csv_open.loc[i, 'cardID'], csv_open.loc[i, 'issued_status']))

show_all()


win.mainloop()
"""     END OF GUI      """
