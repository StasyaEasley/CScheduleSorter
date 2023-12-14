import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd

xxtra_large = ("Rupee", 50)
large_font = ("Rupee", 35)
medium_font = ("Helvetica", 27)
small_font = ("Helvetica", 20)
extra_small_font = ("Helvetica", 15)


class ScheduleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.controller = None
        self.title("Schedule Sorter")
        self.class_dict = None
        self.container = tk.Frame(self)
        self.container.pack(side="left", fill="both", expand=True)
        self.current_page = None
        self.page_history = []
        self.all_selected_items = {}
        self.frames = {}

        for F in (StartPage, PreMajor, CoreCourses, Class_Buttons, Theory,
                  Systems, Paradigms, Electives, Restart):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def set_class_dict(self, my_dict):
        self.class_dict = my_dict

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.page_history.append(cont)
        self.current_page = cont

        if cont == Restart:
            restart_frame = self.frames[cont]
            non_selected_items_label = restart_frame.non_selected_label
            non_selected_items_label[
                "text"] = self.get_non_selected_items_text()

    def get_non_selected_items_text(self):
        non_selected_items = self.frames[Class_Buttons].all_non_selected_items
        max_chars_per_line = 65

        non_selected_text = ""
        for page, items in non_selected_items.items():
            formatted_items = [f"{page}:\n{', '.join(items)}"]
            for line in formatted_items:
                non_selected_text += "\n".join(
                    [line[i:i + max_chars_per_line] for i in
                     range(0, len(line), max_chars_per_line)])
                non_selected_text += "\n"
        return f"Classes to take:\n{non_selected_text}"

    def go_back(self):
        if len(self.page_history) > 1:
            self.page_history.pop()
            prev_page = self.page_history.pop()
            self.set_current_page(prev_page)
            self.show_frame(prev_page)

    def get_next_page(self):
        current_pre_major = self.frames[PreMajor].is_completed()
        current_core_course = self.frames[CoreCourses].is_completed()
        current_theory = self.frames[Theory].is_completed()
        current_systems = self.frames[Systems].is_completed()
        current_paradigms = self.frames[Paradigms].is_completed()

        if current_theory:
            print("Next page: Systems")
            return Systems
        elif current_systems:
            print("Next page: Paradigms")
            return Paradigms
        elif current_paradigms:
            print("Next page: Electives")
            return Electives
        elif current_pre_major:
            selected_items = self.frames[Class_Buttons].selected_items.get(
                self.frames[Class_Buttons].current_page_name, [])
            if "CSC 210" in selected_items and "CSC 244" in selected_items:
                print("Next page: Core Courses")
                return CoreCourses
            elif "CSC 210" in selected_items:
                print("Next page: Core Courses")
                return CoreCourses
            elif not selected_items:
                print("Next Page: Restart")
                return Restart
            else:
                print("Next page: Electives")
                return Electives
        elif current_core_course:
            selected_items = self.frames[Class_Buttons].selected_items.get(
                self.frames[Class_Buttons].current_page_name, [])
            if "CSC 345" in selected_items:
                print("Next page: Theory")
                return Theory
            else:
                print("Next page: Electives")
                return Electives
        else:
            print("Next page: Restart")
            return Restart

    def set_current_page(self, page):
        self.current_page = page


def check_selections(lb):
    selected_items = lb.curselection()
    return selected_items


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="CS Schedule Sorter", font=xxtra_large)
        label.pack(side=tk.TOP)

        schedule = tk.PhotoImage(file='schedule.png')
        photoimage3 = schedule.subsample(3, 3)
        sche = tk.Label(self, image=photoimage3)
        sche.photoimage3 = photoimage3

        sche.pack(side=tk.TOP, padx=30, pady=10)

        message = ttk.Label(self, text="A program designed to help advise "
                                       "\n        UA CS majors on classes. "
                                       "\n\n                Ready to start?",
                            font=medium_font)
        message.pack(side=tk.TOP)

        imag_end = tk.PhotoImage(file='exit_button.png')
        photoimage2 = imag_end.subsample(5, 5)

        exit_button = tk.Button(self, image=photoimage2, height=63, width=142,
                                command=controller.destroy)
        exit_button.image = photoimage2
        exit_button.pack(side="left", anchor=tk.CENTER, padx=35)

        imag_start = tk.PhotoImage(file='start_button.png')
        photoimage1 = imag_start.subsample(5, 5)

        start_button = tk.Button(self, height=63, width=142,
                                 image=photoimage1,
                                 command=lambda: controller.show_frame(
                                     PreMajor), )
        start_button.image = photoimage1
        start_button.pack(side="right", anchor=tk.CENTER, padx=35)
        self.pack_propagate(False)


def button_click(controller, lb, update_method):
    indices = check_selections(lb)
    if update_method == 'update_which':
        controller.frames[Class_Buttons].update_which(indices)
    elif update_method == 'update_2':
        controller.frames[Class_Buttons].update_2(indices)
    elif update_method == 'update_3':
        controller.frames[Class_Buttons].update_3(indices)
    elif update_method == 'update_4':
        controller.frames[Class_Buttons].update_4(indices)
    elif update_method == 'update_5':
        controller.frames[Class_Buttons].update_5(indices)
    elif update_method == 'update_6':
        controller.frames[Class_Buttons].update_6(indices)
    controller.show_frame(Class_Buttons)


class PreMajor(tk.Frame):
    data = ["CSC 110", "CSC 120", "CSC 210", "CSC 144", "CSC 244"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.completed = False
        label = ttk.Label(self,
                          text="Select all that you have taken\n "
                               "    or are currently taking.", font=medium_font)
        label.pack(anchor=tk.CENTER)

        which_class = ttk.Label(self,
                                text="Pre-Major Courses", font=xxtra_large)
        which_class.pack(anchor=tk.CENTER)

        classes = ("CSC 110", "CSC 120", "CSC 210", "CSC 144", "CSC 244")

        lb = Listbox(self, height=5, selectmode='multiple', font=large_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, expand=True)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_which'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: self.update_all_taken(controller))
        other.pack(padx=2, side="right")

    def update_all_taken(self, controller):
        current_page_name = self.__class__.__name__
        all_non_selected_items = controller.frames[
            Class_Buttons].all_non_selected_items

        controller.all_selected_items[current_page_name] = \
            all_non_selected_items[current_page_name]

        controller.frames[Class_Buttons].all_non_selected_items[
            current_page_name] = []

        non_selected_items_label = controller.frames[Restart].non_selected_label
        non_selected_items_label[
            "text"] = controller.get_non_selected_items_text()

        controller.show_frame(CoreCourses)

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class CoreCourses(tk.Frame):
    data = ["CSC 252", "CSC 335", "CSC 345", "CSC 352", "CSC 380"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.completed = None
        label = ttk.Label(self,
                          text="Select all that you have taken\n "
                               "    or are currently taking.", font=medium_font)
        label.pack(anchor="n")

        which_class = ttk.Label(self,
                                text="Core Courses", font=xxtra_large)
        which_class.pack(anchor="n")

        var = StringVar()
        var.set("one")
        classes = ("CSC 252", "CSC 335", "CSC 345", "CSC 352", "CSC 380")
        lb = Listbox(self, height=5, selectmode='multiple', font=large_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, expand=True)

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
                           command=lambda: self.update_all_taken(controller))
        other.pack(padx=2, side="right")

    def update_all_taken(self, controller):
        current_page_name = self.__class__.__name__
        all_non_selected_items = controller.frames[
            Class_Buttons].all_non_selected_items

        controller.all_selected_items[current_page_name] = \
            all_non_selected_items[current_page_name]

        controller.frames[Class_Buttons].all_non_selected_items[
            current_page_name] = []

        non_selected_items_label = controller.frames[Restart].non_selected_label
        non_selected_items_label[
            "text"] = controller.get_non_selected_items_text()

        controller.show_frame(Theory)

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class Theory(tk.Frame):
    data = ["CSC 445", "CSC 450", "CSC 473"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Select all that you have taken\n "
                               "    or are currently taking.", font=medium_font)
        label.pack(anchor="n")

        which_class = ttk.Label(self,
                                text="Theory Courses", font=xxtra_large)
        which_class.pack(anchor="n")

        var = StringVar()
        var.set("one")
        classes = ("CSC 445", "CSC 450", "CSC 473")
        lb = Listbox(self, height=3, selectmode='multiple', font=large_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, expand=True)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(CoreCourses))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_3'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: self.update_all_taken(controller))
        other.pack(padx=2, side="right")

        self.completed = False

    def update_all_taken(self, controller):
        current_page_name = self.__class__.__name__
        all_non_selected_items = controller.frames[
            Class_Buttons].all_non_selected_items

        controller.all_selected_items[current_page_name] = \
            all_non_selected_items[current_page_name]

        controller.frames[Class_Buttons].all_non_selected_items[
            current_page_name] = []

        non_selected_items_label = controller.frames[Restart].non_selected_label
        non_selected_items_label[
            "text"] = controller.get_non_selected_items_text()

        controller.show_frame(Systems)

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class Systems(tk.Frame):
    data = ["CSC 452", "CSC 453"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Select all that you have taken\n "
                               "    or are currently taking.", font=medium_font)
        label.pack(anchor="n")

        which_class = ttk.Label(self,
                                text="Systems Courses", font=xxtra_large)
        which_class.pack(anchor="n")

        var = StringVar()
        var.set("one")
        classes = ("CSC 452", "CSC 453")
        lb = Listbox(self, height=2, selectmode='multiple', font=large_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, expand=True)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(Theory))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_4'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: self.update_all_taken(controller))
        other.pack(padx=2, side="right")

        self.completed = False

    def update_all_taken(self, controller):
        current_page_name = self.__class__.__name__
        all_non_selected_items = controller.frames[
            Class_Buttons].all_non_selected_items

        controller.all_selected_items[current_page_name] = \
            all_non_selected_items[current_page_name]

        controller.frames[Class_Buttons].all_non_selected_items[
            current_page_name] = []

        non_selected_items_label = controller.frames[Restart].non_selected_label
        non_selected_items_label[
            "text"] = controller.get_non_selected_items_text()

        controller.show_frame(Paradigms)

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class Paradigms(tk.Frame):
    data = ["CSC 372", "CSC 422", "CSC 460"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Select all that you have taken\n "
                               "    or are currently taking.", font=medium_font)
        label.pack(anchor="n")

        which_class = ttk.Label(self,
                                text="Paradigm Courses", font=xxtra_large)
        which_class.pack(anchor="n")

        var = StringVar()
        var.set("one")
        classes = ("CSC 372", "CSC 422", "CSC 460")
        lb = Listbox(self, height=3, selectmode='multiple', font=large_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER, expand=True)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(Systems))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_5'))
        next_.pack(side="left", pady=5, padx=20)

        other = ttk.Button(self, text="Click here if all taken",
                           command=lambda: self.update_all_taken(controller))
        other.pack(padx=2, side="right")

        self.completed = False

    def update_all_taken(self, controller):
        current_page_name = self.__class__.__name__
        all_non_selected_items = controller.frames[
            Class_Buttons].all_non_selected_items

        controller.all_selected_items[current_page_name] = \
            all_non_selected_items[current_page_name]

        controller.frames[Class_Buttons].all_non_selected_items[
            current_page_name] = []

        non_selected_items_label = controller.frames[Restart].non_selected_label
        non_selected_items_label[
            "text"] = controller.get_non_selected_items_text()

        controller.show_frame(Electives)

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class Electives(tk.Frame):
    data = ["CSC 317", "CSC 337", "CSC 346",
            "CSC 425", "CSC 433", "CSC 436", "CSC 437",
            "CSC 444", "CSC 447", "CSC 466", "CSC 477",
            "CSC 483", "CSC 480"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select all that you have taken or are "
                                     "currently taking.",
                          font=small_font)
        label.pack(anchor=tk.CENTER, expand=True)

        which_class = ttk.Label(self,
                                text="Elective Courses", font=medium_font)
        which_class.pack(anchor="n")

        reqs = ttk.Label(self, text="One 300/400-level CSC elective,\n "
                                    "two 400-level CSC electives",
                         font=small_font)
        reqs.pack(anchor="n")

        var = StringVar()
        var.set("one")
        classes = ("CSC 317", "CSC 337", "CSC 346",
                   "CSC 425", "CSC 433", "CSC 436", "CSC 437",
                   "CSC 444", "CSC 447", "CSC 466", "CSC 477",
                   "CSC 483", "CSC 480")
        lb = Listbox(self, height=13, selectmode='multiple', font=medium_font)
        for num in classes:
            lb.insert(END, num)
        lb.pack(anchor=tk.CENTER)

        home = ttk.Button(self, text="Home",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="left", pady=5, padx=2)

        back_ = ttk.Button(self, text="Back",
                           command=lambda: controller.show_frame(Paradigms))
        back_.pack(side="left", pady=5, padx=2)

        next_ = ttk.Button(self, text="Next",
                           command=lambda: button_click(controller, lb,
                                                        'update_6'))
        next_.pack(side="right", pady=5, padx=20)

        self.completed = False

    def is_completed(self):
        return self.completed

    def set_completion_status(self, status):
        self.completed = status


class Restart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Congrats!",
                          font=xxtra_large)
        label.pack(anchor="n")

        self.non_selected_label = ttk.Label(self, text="", font=medium_font)
        self.non_selected_label.pack(anchor="n", pady=20)

        home = ttk.Button(self, text="Restart",
                          command=lambda: controller.show_frame(StartPage))
        home.pack(side="top", pady=30)


class Class_Buttons(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.current_page_name = None
        bottom = Frame(self)
        bottom.pack(side=tk.BOTTOM)
        self.controller = controller
        self.label = ttk.Label(self, text="", font=small_font)
        self.label.pack(anchor=tk.CENTER)
        self.home_button = ttk.Button(self, text="Home",
                                      command=self.go_home)
        self.home_button.pack(in_=bottom, side=tk.LEFT, padx=5, pady=5)

        self.back_button = ttk.Button(self, text="Back",
                                      command=self.go_back_2)
        self.back_button.pack(in_=bottom, side=tk.LEFT, padx=20)

        self.next_button = ttk.Button(self, text="Next", command=self.next_page)
        self.next_button.pack(in_=bottom, side=tk.RIGHT, padx=5)

        self.clear_button = ttk.Button(self, text="Clear",
                                       command=self.clear_information)
        self.clear_button.pack(in_=bottom, side=tk.RIGHT, padx=20)

        self.description_frame = tk.Frame(self)
        self.description_frame.pack(pady=10)

        self.description_label = ttk.Label(self.description_frame, text="",
                                           wraplength=400, justify="left",
                                           font=extra_small_font)
        self.description_label.pack(pady=10, anchor=tk.CENTER)

        self.description_buttons = []
        self.completed = False

        self.selected_items = {}
        self.all_selections = {}

        self.all_non_selected_items = {
            page.__name__: getattr(page, 'data', []) for page in
            [PreMajor, CoreCourses, Theory, Systems, Paradigms, Electives]}
        self.original_non_selected = self.all_non_selected_items.copy()

    def clear_information(self):
        self.description_label["text"] = ""

    def go_home(self):
        self.all_selections.clear()
        self.all_non_selected_items = self.original_non_selected
        self.controller.show_frame(StartPage)
        print(self.all_selections)
        print(self.all_non_selected_items)

    def go_back_2(self):
        self.controller.go_back()

    def next_page(self):
        next_page = self.controller.get_next_page()
        self.controller.set_current_page(next_page)
        self.controller.show_frame(next_page)
        print(self.all_selections)
        print(self.all_non_selected_items)

    def update_data(self, indices, classes):
        self.current_page_name = self.controller.current_page.__name__

        selected_items = [classes[i] for i in indices]
        not_selected_values = [classes[i] for i in range(len(classes)) if
                               i not in indices]

        print(
            f"Selections for {self.current_page_name}:"
            f" {', '.join(selected_items)}")
        self.selected_items[self.current_page_name] = selected_items
        self.selected_items[self.controller.current_page] = [classes[i] for i in
                                                             indices]
        descriptions = pd.read_csv('merged_data.tsv', sep='\t')
        descriptions_dict = descriptions.set_index('Class').to_dict(
            orient='index')

        self.all_non_selected_items[self.current_page_name] = (
            not_selected_values)

        print(
            f"Non-selected items for {self.current_page_name}: "
            f"{', '.join(not_selected_values)}")

        self.all_selections[self.current_page_name] = selected_items

        taken_text = ", ".join(selected_items)
        next_steps_text = ", ".join(not_selected_values)

        line_break_interval = 45
        next_steps_formatted = "\n".join(
            [next_steps_text[i:i + line_break_interval] for i in
             range(0, len(next_steps_text), line_break_interval)]
        )

        self.label["text"] = "Taken:\n{}\n\nNext Steps:\n{}".format(
            taken_text, next_steps_formatted)
        self.label["justify"] = "center"
        for button in self.description_buttons:
            button.destroy()

        button_frame = tk.Frame(self.description_frame)
        button_frame.pack()
        new_line_break = 5
        for i, value in enumerate(not_selected_values):
            button = ttk.Button(button_frame, text=value,
                                command=lambda v=value:
                                self.show_description(v, descriptions_dict))

            button.grid(row=i // new_line_break,
                        column=i % new_line_break, padx=5)
            self.description_buttons.append(button)

    # Pre-major Courses
    def update_which(self, indices):
        self.update_data(indices, ["CSC 110", "CSC 120", "CSC 210", "CSC 144",
                                   "CSC 244"])
        self.controller.frames[PreMajor].set_completion_status(True)
        self.controller.frames[CoreCourses].set_completion_status(False)
        self.controller.frames[Theory].set_completion_status(False)
        self.controller.frames[Systems].set_completion_status(False)
        self.controller.frames[Paradigms].set_completion_status(False)
        self.controller.frames[Electives].set_completion_status(False)

    # Core Courses
    def update_2(self, indices):
        self.update_data(indices, ["CSC 252", "CSC 335", "CSC 345", "CSC 352",
                                   "CSC 380"])
        self.controller.frames[PreMajor].set_completion_status(False)
        self.controller.frames[CoreCourses].set_completion_status(True)
        self.controller.frames[Theory].set_completion_status(False)
        self.controller.frames[Systems].set_completion_status(False)
        self.controller.frames[Paradigms].set_completion_status(False)
        self.controller.frames[Electives].set_completion_status(False)

    # Theory Courses
    def update_3(self, indices):
        self.update_data(indices, ["CSC 445", "CSC 450", "CSC 473"])
        # used for the Next button after classes are selected
        self.controller.frames[PreMajor].set_completion_status(False)
        self.controller.frames[CoreCourses].set_completion_status(False)
        self.controller.frames[Theory].set_completion_status(True)
        self.controller.frames[Systems].set_completion_status(False)
        self.controller.frames[Paradigms].set_completion_status(False)
        self.controller.frames[Electives].set_completion_status(False)

    # Systems Courses
    def update_4(self, indices):
        self.update_data(indices, ["CSC 452", "CSC 453"])
        self.controller.frames[PreMajor].set_completion_status(False)
        self.controller.frames[CoreCourses].set_completion_status(False)
        self.controller.frames[Theory].set_completion_status(False)
        self.controller.frames[Systems].set_completion_status(True)
        self.controller.frames[Paradigms].set_completion_status(False)
        self.controller.frames[Electives].set_completion_status(False)

    # Paradigm Courses
    def update_5(self, indices):
        self.update_data(indices, ["CSC 372", "CSC 422", "CSC 460"])
        self.controller.frames[PreMajor].set_completion_status(False)
        self.controller.frames[CoreCourses].set_completion_status(False)
        self.controller.frames[Theory].set_completion_status(False)
        self.controller.frames[Systems].set_completion_status(False)
        self.controller.frames[Paradigms].set_completion_status(True)
        self.controller.frames[Electives].set_completion_status(False)

    # Elective Courses
    def update_6(self, indices):
        self.update_data(indices, ["CSC 317", "CSC 337", "CSC 346",
                                   "CSC 425", "CSC 433", "CSC 436", "CSC 437",
                                   "CSC 444", "CSC 447", "CSC 466", "CSC 477",
                                   "CSC 483", "CSC 480"])
        self.controller.frames[PreMajor].set_completion_status(False)
        self.controller.frames[CoreCourses].set_completion_status(False)
        self.controller.frames[Theory].set_completion_status(False)
        self.controller.frames[Systems].set_completion_status(False)
        self.controller.frames[Paradigms].set_completion_status(False)
        self.controller.frames[Electives].set_completion_status(True)

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

app = ScheduleApp()
app.set_class_dict(class_dict)
app.mainloop()
