import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd

large_font = ("Rupee", 35)
medium_font = ("Helvetica", 27)
small_font = ("Helvetica", 20)
extra_small_font = ("Helvetica", 15)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.class_dict = None
        self.container = tk.Frame(self)
        self.container.pack(side="left", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, Page1, Page3, Page4):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def set_class_dict(self, my_dict):
        self.class_dict = my_dict

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

        schedule = tk.PhotoImage(file='schedule.png')
        photoimage3 = schedule.subsample(3, 3)
        sche = tk.Label(self, image=photoimage3)
        sche.photoimage3 = photoimage3  # To keep a reference to the image

        sche.pack(side=tk.TOP, padx=30, pady=10)

        imag_end = tk.PhotoImage(file='exit_button.png')
        photoimage2 = imag_end.subsample(5, 5)

        button2 = tk.Button(self, image=photoimage2, height=63, width=142,
                            command=controller.destroy)
        button2.image = photoimage2
        button2.pack(side="left", anchor="center", padx=65)

        imag_start = tk.PhotoImage(file='start_button.png')
        photoimage1 = imag_start.subsample(5, 5)

        button1 = tk.Button(self, height=63, width=142,
                            image=photoimage1,
                            command=lambda: controller.show_frame(Page1), )
        button1.image = photoimage1
        button1.pack(side="left", anchor="center")


def next_button_click(controller, lb):
    indices = check_selections(controller, lb)
    controller.frames[Page4].update_which(indices)
    controller.show_frame(Page4)


def new_button(controller, lb):
    indices = check_selections(controller, lb)
    controller.frames[Page4].update_2(indices)
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

        lb = Listbox(self, height=5, selectmode='multiple', font=medium_font)
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, fill=BOTH)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: next_button_click(controller,
                                                             lb))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Page3))
        other.pack(padx=2, side="right")


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken or are "
                                     "currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 252", "CSC 335", "CSC 345", "CSC 352", "CSC 380")
        lb = Listbox(self, height=5, selectmode='multiple', font=medium_font)
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, fill=BOTH)

        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(Page1))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: new_button(controller,
                                                      lb))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Page1))
        other.pack(padx=2, side="right")


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.label = ttk.Label(self, text="", font=small_font)
        self.label.pack(anchor="n")

        ttk.Button(self, text="Home",
                   command=lambda: controller.show_frame(StartPage)).pack(
            padx=2, anchor=tk.SW)
        ttk.Button(self, text="Back",
                   command=lambda: controller.show_frame(Page1)).pack(padx=2,
                                                                      anchor=tk.SW)

        self.description_frame = tk.Frame(self)
        self.description_frame.pack(pady=10)

        self.description_label = ttk.Label(self.description_frame, text="",
                                           wraplength=400, justify="left",
                                           font=extra_small_font)
        self.description_label.pack(pady=10)

        self.description_buttons = []

    def update_data(self, indices, classes):
        descriptions = pd.read_csv('merged_data.tsv', sep='\t')
        descriptions_dict = descriptions.set_index('Class').to_dict(
            orient='index')

        selected_values = [classes[i] for i in indices]
        not_selected_values = [classes[i] for i in range(len(classes)) if
                               i not in indices]

        self.label["text"] = "Taken: {}\nNext Steps: {}".format(
            ", ".join(selected_values), ", ".join(not_selected_values))

        for button in self.description_buttons:
            button.destroy()

        for value in not_selected_values:
            button = ttk.Button(self, text=value, command=lambda
                v=value: self.show_description(v, descriptions_dict))
            button.pack(side="left", padx=5)
            self.description_buttons.append(button)

    def update_which(self, indices):
        self.update_data(indices, ["CSC 110", "CSC 120", "CSC 210", "CSC 144",
                                   "CSC 244"])

    def update_2(self, indices):
        self.update_data(indices, ["CSC 252", "CSC 335", "CSC 345", "CSC 352",
                                   "CSC 380"])

    def show_description(self, value, my_dict):
        if value in my_dict:
            info = my_dict[value]
            full_description = f"Class: {value}\n\n" + "\n".join(
                f"{header}: {info[header]}\n" for header in info)

            xxx_small_font = ("Helvetica", 13)
            self.description_label.configure(font=xxx_small_font)

            self.description_label["text"] = full_description
        else:
            self.label["text"] = f"No information available for {value}"
            self.description_label["text"] = ""


descriptions_df = pd.read_csv('merged_data.tsv', sep='\t', index_col='Career')

class_dict = {}

for index, row_data in descriptions_df.iterrows():
    class_name = row_data['Class']
    class_info = {header: row_data[header] for header in row_data.index}
    class_dict[class_name] = class_info

app = tkinterApp()
app.set_class_dict(class_dict)
app.mainloop()
