from tkinter import *


# Create classes to represent the Welcome Page, User Input Page, and Results Page
class WelcomePage:
    def __init__(self, master):
        # Prevent user from changing the window size
        master.geometry("750x750")  # Gives a starting geometry to the window
        master.resizable(width=False, height=False)

        # Initialize Frames
        title_frame = Frame(master, height=250, width=750)
        title_frame.pack()
        input_frame = Frame(master, height=500, width=750)
        input_frame.pack()

        # Create welcome screen text labels
        self.title_label = Label(title_frame, text="New York City Property Value Predictor", bg="darkblue", fg="white")
        self.title_label.config(height=5, width=40)
        self.title_label.config(font=("Courier bold", 30))
        self.title_label.pack()
        self.text_label = Label(title_frame, text="Please enter the following property information to receiving a "
                                             "purchase price prediction.", bg="lightgray", wraplength=725)
        self.text_label.config(height=5, width=60)
        self.text_label.config(font=("Courier", 20))
        self.text_label.pack()

        self.space_label = Label(title_frame)
        self.space_label.pack()

        # Create borough drop down list
        self.borough = StringVar(input_frame)
        self.borough.set("                         ")

        self.borough_label = Label(input_frame, text="Borough: ")
        self.borough_label.grid(row=0, column=0)

        self.borough_dropdown = OptionMenu(input_frame, self.borough, "Manhattan", "The Bronx", "Brooklyn", "Queens", "Staten Island")
        self.borough_dropdown.grid(row=0, column=1, sticky=W)

        # Create neighborhood drop down list (based on borough)
        self.neighborhood = StringVar(input_frame)
        self.neighborhood.set("                         ")

        self.neighborhood_label = Label(input_frame, text="Neighborhood: ")
        self.neighborhood_label.grid(row=1, column=0)

        self.neighborhood_dropdown = OptionMenu(input_frame, self.neighborhood, "")
        self.neighborhood_dropdown.grid(row=1, column=1, sticky=W)

        # Create user entry field for Year Built
        self.year_label = Label(input_frame, text="Year Built: ")
        self.year_label.grid(row=2, column=0)

        self.year_entry = Entry(input_frame)
        self.year_entry.grid(row=2, column=1)

        # Create user entry for land square feet
        self.land_label = Label(input_frame, text="Land Square Feet: ")
        self.land_label.grid(row=3, column=0)

        self.land_entry = Entry(input_frame)
        self.land_entry.grid(row=3, column=1)

        # Create user entry for gross square feet
        self.gross_label = Label(input_frame, text="Gross Square Feet: ")
        self.gross_label.grid(row=4, column=0)

        self.gross_entry = Entry(input_frame)
        self.gross_entry.grid(row=4, column=1)

        # Create command buttons for the application
        self.continue_button = Button(input_frame, text="Continue", command=getUserValues)
        self.continue_button.grid(columnspan=3)

        self.quit_button = Button(input_frame, text="Quit")
        self.quit_button.grid(columnspan=3)

        # Create year restriction message
        self.year_restrict = Label(input_frame, text="*Year cannot be greater than 2020*", font=("Times New Roman",12))
        self.year_restrict.grid(columnspan=3)



class ResultsPage:
    def __init__(self, master):
        pass



def getUserValues():
    y = welcome.borough.get()
    print(y)
    x = welcome.year_entry.get()
    print(x)

# Create the base window
base = Tk()

# Create
welcome = WelcomePage(base)

base.mainloop()
