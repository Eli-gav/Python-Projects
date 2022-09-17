import tkinter as tk
from tkinter import *
import webbrowser
#new
from tkinter import ttk



class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        #new us
        self.entry = Entry(self.master, width= 42)
        self.entry.grid(padx=(10,10), pady=(20,20))
        
        
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

        #new
        self.btn=Button(self.master, text="Submit Custom Text", width=30,height=2,command=self.customHTML)
        self.btn.grid(padx=(10,10), pady=(5,5))
      

    def defaultHTML(self):
        htmlText="Stay tuned for our amazing summer sale!"
        htmlFile=open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        #new
        

    def customHTML(self):
        htmlText=self.entry.get()
        htmlFile=open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




    

   


if __name__ == "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
