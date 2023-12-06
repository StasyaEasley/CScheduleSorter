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

        for F in (StartPage, PreMajor, Core_course, Class_buttons, Theory,
                  Systems, Paradigms):
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
        sche.photoimage3 = photoimage3

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
                            command=lambda: controller.show_frame(PreMajor), )
        button1.image = photoimage1
        button1.pack(side="left", anchor="center")


def button_click(controller, lb, update_method):
    indices = check_selections(controller, lb)
    if update_method == 'update_which':
        controller.frames[Class_buttons].update_which(indices)
    elif update_method == 'update_2':
        controller.frames[Class_buttons].update_2(indices)
    elif update_method == 'update_3':
        controller.frames[Class_buttons].update_3(indices)
    elif update_method == 'update_4':
        controller.frames[Class_buttons].update_4(indices)
    elif update_method == 'update_5':
        controller.frames[Class_buttons].update_5(indices)
    controller.show_frame(Class_buttons)


class PreMajor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self,
                          text="Select all that you have taken or are "
                               "currently taking.", font=small_font)
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
                           command=lambda: button_click(controller, lb,
                                                        'update_which'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Core_course))
        other.pack(padx=2, side="right")


class Core_course(tk.Frame):
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
                           command=lambda: controller.show_frame(PreMajor))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_2'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Theory))
        other.pack(padx=2, side="right")


class Theory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken or are "
                                     "currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 445", "CSC 450", "CSC 473")
        lb = Listbox(self, height=3, selectmode='multiple', font=medium_font)
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(PreMajor))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_3'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Systems))
        other.pack(padx=2, side="right")


class Systems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken or are "
                                     "currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 452", "CSC 453")
        lb = Listbox(self, height=2, selectmode='multiple', font=medium_font)
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(PreMajor))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_4'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(Paradigms))
        other.pack(padx=2, side="right")


class Paradigms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken or are "
                                     "currently taking.",
                          font=small_font)
        label.pack(anchor="n")
        var = StringVar()
        var.set("one")
        data = ("CSC 372", "CSC 422", "CSC 460")
        lb = Listbox(self, height=3, selectmode='multiple', font=medium_font)
        for num in data:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(PreMajor))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_5'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: controller.show_frame(PreMajor))
        other.pack(padx=2, side="right")


class Class_buttons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.label = ttk.Label(self, text="", font=small_font)
        self.label.pack(anchor="n")

        ttk.Button(self, text="Home",
                   command=lambda: controller.show_frame(StartPage)).pack(
            padx=2, anchor=tk.SW)
        ttk.Button(self, text="Back",
                   command=lambda: controller.show_frame(PreMajor)).pack(padx=2,
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

    # Pre-major Courses
    def update_which(self, indices):
        self.update_data(indices, ["CSC 110", "CSC 120", "CSC 210", "CSC 144",
                                   "CSC 244"])

    # Core Courses
    def update_2(self, indices):
        self.update_data(indices, ["CSC 252", "CSC 335", "CSC 345", "CSC 352",
                                   "CSC 380"])

    # Theory Courses
    def update_3(self, indices):
        self.update_data(indices, ["CSC 445", "CSC 450", "CSC 473"])

    # Systems Courses
    def update_4(self, indices):
        self.update_data(indices, ["CSC 452", "CSC 453"])

    # Paradigm Courses
    def update_5(self, indices):
        self.update_data(indices, ["CSC 372", "CSC 422", "CSC 460"])

    # Elective Courses
    def update_6(self, indices):
        self.update_data(indices, ["CSC 250", "CSC 337", "CSC 346", "317",
                                   "CSC 425", "CSC 433", "CSC 436", "CSC 437",
                                   "CSC 444", "CSC 447",  "CSC 466", "CSC 477",
                                   "CSC 483", "CSC 480"])

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
