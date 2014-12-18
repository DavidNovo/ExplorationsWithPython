# tkinter and tcl
# making windows
# lesson 39 of beginning python
# lesson 40 making buttons
# lesson 41 tkinter event handling
from tkinter import *

# making a Window class
# this class is for creating the window
class Window(Frame):

    # defining the initialize method
    # this is run first by container
    def __init__(self, master = NONE):
        # creating the frame in the  window
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    # this method adds buttons to the frame
    def init_window(self):
        self.master.title("GUI")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button

        # adding event handling to a button lesson 41
        quitButton = Button(self,text="Quit",command = self.client_exit)
        quitButton.place(x=0,y=0)

        # make a main menu
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)

        fileDropDown = Menu(menuBar)
        menuBar.add_cascade(label='File', menu=fileDropDown)
        fileDropDown.add_command(label='Exit', command=self.client_exit)


        editDropDown = Menu(menuBar)
        menuBar.add_cascade(label='Edit', menu=editDropDown)
        editDropDown.add_command(label='Undo')




    def client_exit(self):
        exit()


#
# naming the root
root = Tk()

# size off the window
root.geometry("400x300")

# using the Window class with our defined root
# the self variable is set to root
# the second variable is left as the default
# in this case the default is master = None
app = Window(root)

# the execution happens here
root.mainloop()


