from tkinter import *

# Create classes to represent the Welcome Page, User Input Page, and Results Page
class WelcomePage:
    def __init__(self, master):
        # Prevent user from changing the window size
        master.geometry("750x750")  # Gives a starting geometry to the window
        master.resizable(width=False, height=False)

        # Initialize Frames
        #title_frame = Frame(master)
        #title_frame.pack()
        #text_frame = Frame(master)
        #text_frame.pack(side=BOTTOM)

        # Create welcome screen text labels
        self.title_label = Label(master, text="New York City Property Value Predictor", bg="darkblue", fg="white")
        self.title_label.config(height=5, width=40)
        self.title_label.config(font=("Courier", 30))
        self.title_label.pack()
        self.text_label = Label(master, text="Please enter the following property information to receiving a "
                                             "purchase price prediction.", bg="lightgray", wraplength=725)
        self.text_label.config(height=5, width=60)
        self.text_label.config(font=("Courier", 20))
        self.text_label.pack()


        # Create buttons to continue the application
        self.continue_button = Button(master, text="Continue")
        self.continue_button.pack()
        self.quit_button = Button(master, text="Quit")
        self.quit_button.pack()

class UserInputPage:
    def __init__(self, master):
        pass


class ResultsPage:
    def __init__(self, master):
        pass


# Create the base window
base = Tk()

# Create
welcome = WelcomePage(base)

base.mainloop()