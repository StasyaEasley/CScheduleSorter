import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd

large_font = ("Rupee", 35)
small_font = ("Helvetica", 20)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def check_selections(controller, lb):
    selected_items = lb.curselection()
    return selected_items


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="CS Schedule Sorter", font=large_font)
        label.pack(side=tk.TOP)

        imag_start = tk.PhotoImage(file='start_button.png')
        photoimage1 = imag_start.subsample(5, 5)

        button1 = ttk.Button(self, image=photoimage1,
                             command=lambda: controller.show_frame(Page1))
        button1.image = photoimage1
        button1.pack(pady=10)

        imag_end = tk.PhotoImage(file='exit_button.png')
        photoimage2 = imag_end.subsample(5, 5)

        button2 = ttk.Button(self, image=photoimage2,
                             command=controller.destroy)
        button2.image = photoimage2
        button2.pack(pady=10)


def next_button_click(controller, lb):
    indices = check_selections(controller, lb)
    controller.frames[Page4].update_which(indices)
    controller.show_frame(Page4)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self,
                          text="Select all that you have taken or are "
                               "currently taking.",
                          font=small_font)
        label.pack(anchor="n")

        data = ("CSC 110", "CSC 120", "CSC 210", "CSC 144", "CSC 244")

        lb = Listbox(self, height=5, selectmode='multiple')
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, padx=5)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(pady=5)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: next_button_click(controller,
                                                             lb))
        next_.pack(pady=5)

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


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.label = ttk.Label(self, text="", font=small_font)
        self.label.pack(anchor="n")

        self.home_button = ttk.Button(self, text="Home",
                                      command=lambda: controller.show_frame(
                                          StartPage))
        self.home_button.pack(pady=10)

        self.back_button = ttk.Button(self, text="Back",
                                      command=lambda: controller.show_frame(
                                          Page1))
        self.back_button.pack(pady=10)

        self.description_frame = tk.Frame(self)
        self.description_frame.pack(pady=10)

        self.description_label = ttk.Label(self.description_frame, text="",
                                           wraplength=200, justify="left",
                                           font=small_font)
        self.description_label.pack(pady=10)

        self.description_buttons = []

    def update_which(self, indices):
        descriptions_df = pd.read_csv('merged_data.tsv', sep='\t',
                                      index_col='Class')
        descriptions_dict = descriptions_df.set_index('Class Name')['Description'].to_dict()

        for index in indices:
            class_code = descriptions_df.index[index]
            description = get_class_description(class_code, descriptions_dict)
            self.label["text"] = description

        classes = ("CSC 110", "CSC 120", "CSC 210", "CSC 144", "CSC 244")
        selected_values = [classes[index] for index in indices]
        not_selected_values = [classes[i] for i in range(len(classes)) if
                               i not in indices]

        self.label["text"] = "Selected: {}\nNext Steps: {}".format(
            ", ".join(selected_values),
            ", ".join(not_selected_values))

        # Remove existing buttons
        for button in self.description_buttons:
            button.destroy()

        # Create buttons for not selected values
        for value in not_selected_values:
            button = ttk.Button(self, text=value,
                                command=lambda v=value: self.show_description(
                                    v, descriptions_df))
            button.pack(pady=5)
            self.description_buttons.append(button)

        print(descriptions_dict)

    def show_description(self, value, descriptions_dict):
        description = get_class_description(value, descriptions_dict)
        self.description_label["text"] = description


def get_class_description(class_name, descriptions_dict):
    return descriptions_dict.get(class_name, "No description available.")


# Define a function to get the description for a class


app = tkinterApp()
app.mainloop()
