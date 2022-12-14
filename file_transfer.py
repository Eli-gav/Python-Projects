
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
#new
import datetime
import time

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        #Sets title of GUi window
        self.master.title("File Transfer")
        #Creates button to select files from scource directory
        self.sourceDir_btn = Button(text='Select Source', width=20, command=self.sourceDir)
        #Position source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0,padx=(20,10),pady=(30,0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx/pady are the same
        self.source_dir.grid(row=0,column=1,columnspan=2,padx=(20,10),pady=(30,0))

        #Creates button to select destination of files
        self.destDir_btn =Button(text='Select Destination', width=20, command=self.destDir)
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1,column=1,columnspan=2,padx=(20,10),pady=(15,10))

        self.transfer_btn= Button(text='Transfer Files', width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1,padx=(200,0),pady=(0,15))

        self.exit_btn = Button(text='Exit', width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))


    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .deleted(0,END) will clear content
        self.source_dir.delete(0,END)
        self.source_dir.insert(0,selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        source = self.source_dir.get()
        destination=self.destination_dir.get()
        source_files=os.listdir(source)
        for i in source_files:
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')
        #Date time 
        path = '\Python_Projects\Customer Source'
        modification_time = os.path.getmtime(path)
        print("Last modification in 24hours: \n", access_time)
            

    def exit_program(self):
        root.destroy()
        

if __name__ == "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
