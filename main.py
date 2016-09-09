# Imports
from tkinter import *
import mysql.connector


# Variable
__author__ = "hiperbolt"
cnx = mysql.connector.connect()
cursor = cnx.cursor()
root = Tk()
root.geometry('500x400')
root.title('Spoon Counter')


# Main Class
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func

def main():
    while 1 == 1:
        query = ("SELECT count FROM count")
        cursor.execute(query)

        for (count) in cursor:
            frame1 = Frame(root)
            frame2 = Frame(root)
            label1 = Label(frame1, text='Count:')
            label2 = Label(frame2, text='%s' % count)
            button1 = Button(frame2, text='Add Spoon', command=lambda: combine_funcs(frame1.pack_forget(), frame2.pack_forget(), addcount()))
            frame1.pack()
            frame2.pack()
            label1.pack()
            label2.pack()
            button1.pack()
            root.mainloop()

def addcount():
    query = ("UPDATE count SET count = count+1")
    cursor.execute(query)
    cnx.commit()
    main()

main()
