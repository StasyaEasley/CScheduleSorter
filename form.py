import tkinter as tk
from tkinter import *
from tkinter import ttk

largefont = ("Rupee", 35)
small_font = ("Helvetica", 20)


# Rupee,


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # start-page, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame start-page

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=BOTH, expand=True)

        # label of frame Layout 2
        label = ttk.Label(self, text="CS Schedule Sorter",
                          font=largefont)
        label.pack(side=tk.TOP)

        schedule = tk.PhotoImage(file='schedule.png')
        photoimage3 = schedule.subsample(3, 3)
        sche = tk.Label(self, image=photoimage3)
        sche.photoimage3 = photoimage3  # To keep a reference to the image

        sche.pack(side=tk.TOP, padx=30, pady=10)
        # putting the grid in its place by using
        # grid
        imag_start = tk.PhotoImage(file='start_button.png')
        photoimage1 = imag_start.subsample(5, 5)

        button1 = ttk.Button(self, image=photoimage1,
                             command=lambda: controller.show_frame(Page1))
        button1.image = photoimage1

        # putting the button in its place by
        # using grid
        button1.pack(in_=bottom, side=RIGHT, padx=10)

        imag_end = tk.PhotoImage(file='exit_button.png')
        photoimage2 = imag_end.subsample(5, 5)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, image=photoimage2,
                             command=controller.destroy)
        button2.image = photoimage2

        # putting the button in its place by
        # using grid
        button2.pack(in_=bottom, side=LEFT, padx=10)


# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken \n     "
                                     "  or are currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 110", "CSC 120", "CSC 210", "CSC 144", "CSC 244")

        lb = Listbox(self, height=5, selectmode='multiple')
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, padx=5)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(padx=2, anchor=tk.CENTER)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: controller.show_frame(Page2))
        next_.pack(padx=2, anchor=tk.CENTER)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Page3))
        other.pack(padx=2, anchor=tk.NE)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="other",
                          font=small_font)
        label.pack(padx=5, pady=10, side=tk.TOP)
        var = StringVar()
        var.set("one")
        data = "other", "other"

        lb = Listbox(self, height=5, selectmode='multiple')
        for num in data:
            lb.insert(END, num)
        lb.pack(padx=5, pady=10, side=tk.RIGHT)

        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack(padx=5, pady=10, side=tk.LEFT)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken \n     "
                                     "  or are currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 252", "CSC 335", "CSC 345", "CSC 352", "CSC 380")

        lb = Listbox(self, height=5, selectmode='multiple')
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, padx=5)

        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack(padx=2, anchor=tk.CENTER)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(Page1))
        back_.pack(padx=2, anchor=tk.CENTER)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: controller.show_frame(Page1))
        next_.pack(padx=2, anchor=tk.CENTER)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Page3))
        other.pack(padx=2, anchor=tk.NE)


# Driver Code
app = tkinterApp()
app.mainloop()
