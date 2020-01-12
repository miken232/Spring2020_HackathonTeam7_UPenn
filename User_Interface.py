from tkinter import *
import time
from datetime import date
# The Python file that initiates and displays the user interfaces.  The user is prompted to enter certain
# information pertaining to a property they are researching in New York City.  Once the user has entered all of
# the relevant information, they can continue to the results where their predicted price will be displayed.

# Create a class to represent the Welcome Page where the user will enter the property's information
class WelcomePage:
    def __init__(self):
        # Create the master window and its title
        self.master = Tk()
        self.master.title("New York City Price Predictor")

        # Initiate the list which will record the user's entered data
        self.user_data = []

        # Prevent user from changing the window size
        self.master.geometry("750x750")  # Gives a starting geometry to the window
        self.master.resizable(width=False, height=False)

        # Initialize Frames
        self.title_frame = Frame(self.master, height=250, width=750)
        self.title_frame.pack()
        self.input_frame = Frame(self.master, height=500, width=750)
        self.input_frame.pack()

        # Create welcome screen text labels
        self.title_label = Label(self.title_frame, text="New York City Property Value Predictor", bg="darkblue", fg="white")
        self.title_label.config(height=5, width=40)
        self.title_label.config(font=("Courier bold", 30))
        self.title_label.pack()
        self.text_label = Label(self.title_frame, text="Please enter the following property information to receive a "
                                             "purchase price prediction.", bg="lightgray", wraplength=725)
        self.text_label.config(height=5, width=60)
        self.text_label.config(font=("Courier", 20))
        self.text_label.pack()

        self.space_label = Label(self.title_frame)
        self.space_label.pack()

        # Create borough drop down list
        boroughs = ["Manhattan", "The Bronx", "Brooklyn", "Queens", "Staten Island"]
        self.borough = StringVar(self.input_frame)
        self.borough.set("                         ")

        self.borough_label = Label(self.input_frame, text="Borough: ")
        self.borough_label.grid(row=0, column=0, sticky=E)

        self.borough_dropdown = OptionMenu(self.input_frame, self.borough, *boroughs, command=self.updateNeighborhoodList)
        self.borough_dropdown.grid(row=0, column=1, sticky=W)

        # Create neighborhood drop down list (based on borough)
        self.neighborhood = StringVar(self.input_frame)
        self.neighborhood.set("(Please Select a Borough)")

        self.neighborhood_label = Label(self.input_frame, text="Neighborhood: ")
        self.neighborhood_label.grid(row=1, column=0, sticky=E)

        self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, "")
        self.neighborhood_dropdown.grid(row=1, column=1, sticky=W)

        # Create a user entry field for Building Class
        building_classes = ["01 ONE FAMILY DWELLINGS" ,"02 TWO FAMILY DWELLINGS" ,"03 THREE FAMILY DWELLINGS",
                            "04 TAX CLASS 1 CONDOS", "05 TAX CLASS 1 VACANT LAND", "06 TAX CLASS 1 - OTHER",
                            "07 RENTALS - WALKUP APARTMENTS", "08 RENTALS - ELEVATOR APARTMENTS", "09 COOPS - WALKUP APARTMENTS",
                            "10 COOPS - ELEVATOR APARTMENTS", "11 SPECIAL CONDO BILLING LOTS", "11A CONDO-RENTALS",
                            "12 CONDOS - WALKUP APARTMENTS", "13 CONDOS - ELEVATOR APARTMENTS", "14 RENTALS - 4-10 UNIT",
                            "15 CONDOS - 2-10 UNIT RESIDENTIAL", "16 CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT", "17 CONDO COOPS",
                            "18 TAX CLASS 3 - UNTILITY PROPERTIES", "21 OFFICE BUILDINGS", "22 STORE BUILDINGS",
                            "23 LOFT BUILDINGS", "25 LUXURY HOTELS", "26 OTHER HOTELS", "27 FACTORIES",
                            "28 COMMERCIAL CONDOS", "29 COMMERCIAL GARAGES", "30 WAREHOUSES", "31 COMMERCIAL VACANT LAND",
                            "32 HOSPITAL AND HEALTH FACILITIES", "33 EDUCATIONAL FACILITIES", "34 THEATRES",
                            "35 INDOOR PUBLIC AND CULTURAL FACILITIES", "36 OUTDOOR RECREATIONAL FACILITIES",
                            "37 RELIGIOUS FACILITIES", "38 ASYLUMS AND HOMES", "39 TRANSPORTATION FACILITIES",
                            "40 SELECTED GOVERNMENTAL FACILITIES", "41 TAX CLASS 4 - OTHER", "42 CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC",
                            "43 CONDO OFFICE BUILDINGS", "44 CONDO PARKING", "45 CONDO HOTELS", "46 CONDO STORE BUILDINGS",
                            "47 CONDO NON-BUSINESS STORAGE", "48 CONDO TERRACES/GARDENS/CABANAS", "49 CONDO WAREHOUSES/FACTORY/INDUS"]
        reduced_building_classes = ["04 TAX CLASS 1 CONDOS", "07 RENTALS - WALKUP APARTMENTS", "08 RENTALS - ELEVATOR APARTMENTS",
                                   "09 COOPS - WALKUP APARTMENTS", "10 COOPS - ELEVATOR APARTMENTS", "11A CONDO-RENTALS",
                                   "12 CONDOS - WALKUP APARTMENTS", "13 CONDOS - ELEVATOR APARTMENTS",
                                   "14 RENTALS - 4-10 UNIT", "15 CONDOS - 2-10 UNIT RESIDENTIAL"]
        self.building = StringVar(self.input_frame)
        self.building.set("                         ")

        self.building_label = Label(self.input_frame, text="Building Class: ")
        self.building_label.grid(row=2, column=0, sticky=E)

        self.building_dropdown = OptionMenu(self.input_frame, self.building, *reduced_building_classes)
        self.building_dropdown.grid(row=2, column=1, sticky=W)

        # Create user entry field for Year Built
        self.year_label = Label(self.input_frame, text="Year Built: ")
        self.year_label.grid(row=3, column=0, sticky=E)

        self.year_entry = Entry(self.input_frame)
        self.year_entry.grid(row=3, column=1, sticky=W)

        # Create user entry for land square feet
        self.unit_label = Label(self.input_frame, text="Number of Residential Units: ")
        self.unit_label.grid(row=4, column=0, sticky=E)

        self.unit_entry = Entry(self.input_frame)
        self.unit_entry.grid(row=4, column=1, sticky=W)

        # Create user entry for gross square feet
        self.gross_label = Label(self.input_frame, text="Gross Square Feet: ")
        self.gross_label.grid(row=5, column=0, sticky=E)

        self.gross_entry = Entry(self.input_frame)
        self.gross_entry.grid(row=5, column=1, sticky=W)

        # Create command buttons for the application
        self.continue_button = Button(self.input_frame, text="Continue", command=self.decision)
        self.continue_button.grid(row=6, column=0, sticky=E)

        self.quit_button = Button(self.input_frame, text="Quit", command=quit)
        self.quit_button.grid(row=6, column=1, sticky=W)

        # Create year restriction message
        self.year_restrict = Label(self.input_frame, text="*Year cannot be greater than 2020*", font=("Times New Roman",12))
        self.year_restrict.grid(columnspan=3)

        # Create an error message if the user doesn't fill in all fields, but hide it from sight
        self.error = Label(self.input_frame, text="*Please fill in all fields to continue*", fg="white", font=("Times New Roman bold", 18))
        self.error.grid(columnspan=3)

        # Keep the welcome page running until the user exits
        self.master.mainloop()

    # Create a function which decides on the action to take depending on when the "continue" button us pressed
    def decision(self):
        try:
            error_marker = False
            # Remind user that year must be less than 2020
            if self.year_entry.get() == "" or int(self.year_entry.get()) > 2020:
                self.year_restrict.config(fg="red", font=("Times New Roman bold", 18))
                error_marker = True

            #Remind user to fill in all fields
            if self.borough.get() == "" or self.neighborhood.get() == "" or self.building.get() == "" or self.unit_entry.get() == "" or self.gross_entry == "":
                self.error.destroy()
                self.error = Label(self.input_frame, text="Please fill in all fields to continue", fg="red" ,font=("Times New Roman bold", 18))
                self.error.grid(columnspan=3)
                error_marker = True

            # If there are no errors, record the user's entered values in the correct form, and continue to the model
            if error_marker == False:
                self.getUserValues()

        except ValueError:
            self.error.destroy()
            self.error = Label(self.input_frame, text="Please fill in all fields correctly.", fg="red",
                               font=("Times New Roman bold", 18))
            self.error.grid(columnspan=3)

    # Create a function to automatically update the neighborhood dropdown list when a different borough is selected
    def updateNeighborhoodList(self, *args):
        manhattan_neighborhoods = ["Alphabet City", "Chelsea", "ChinaTown", "Civic Center", "Clinton", "East Village",
                                   "Fashion", "Financial", "Flatiron", "Gramercy", "Greenwhich Village - Central",
                                   "Greenwhich Village - West",
                                   "Harlem - Central", "Harmlem - East", "Harlem - Upper", "Harlem - West", "Inwood",
                                   "Javits Center", "Kips Bay", "Little Italy", "Lower East Side", "Manhattan Valley",
                                   "Midtown CBD", "Midtown East", "Midtown West", "Morningside Heights", "Murray Hill",
                                   "Roosevelt Island", "Soho", "Southbridge", "Tribeca", "Upper East Side (59-79)",
                                   "Upper East Side (79-96)", "Upper East Side (96-110)", "Upper West Side (59-79)",
                                   "Upper West Side (79-96)", "Upper West Side (96-110)", "Washington Heights Lower",
                                   "Washington Heights Upper"]
        bronx_neighborhoods = ["Bathgate", "Baychester", "Bedford Park/Norwood", "Belmont", "Bronx Park", "Bronxdale",
                               "Castle Hill/Unionport", "City Island", "City Island-Pelham Strip", "Co-Op City",
                               "Country Club",
                               "Crotona Park", "East River", "East Tremont", "Fieldston", "Fordham",
                               "Highbridge/Morris Heights",
                               "Hunts Point", "Kingsbridge HTS/Univ HTS", "Kingsbridge/Jerome Park",
                               "Melrose/Concourse",
                               "Morris Park/Van Nest", "Morrisania/Longwood", "Mott Haven/Port Morris",
                               "Mount Hope/Mount Eden",
                               "Parkchester", "Pelham Bay", "Pelham Gardens", "Pelham Parkway North",
                               "Pelham Parkway South",
                               "Riverdale", "Schuylerville/Pelham Bay", "Sound View", "Throgs Neck",
                               "Van CortlandT Park",
                               "Wakefield", "Westchester", "Williamsbridge", "Woodlawn"]
        brooklyn_neighborhoods = ["Bath Beach", "Bay Ridge", "Bedford Stuyvesant", "Bensonhurst", "Bergen Beach",
                                  "Boerum Hill",
                                  "Borough Park", "Brighton Beach", "Brooklyn Heights", "Brownsville", "Bush Terminal",
                                  "Bushwick",
                                  "Canarsie", "Carroll Gardens", "Clinton Hill", "Cobble Hill", "Cobble Hill-West",
                                  "Coney Island",
                                  "Crown Heights", "Cypress Hills", "Downtown-Fulton Ferry", "Downtown-Fulton Mall",
                                  "Downtown-Metrotech",
                                  "Dyker Heights", "East New York", "Flatbush-Central", "Flatbush-East",
                                  "Flatbush-Lefferts Garden",
                                  "Flatbush-North", "Flatlands", "Fort Greene", "Gerritsen Beach", "Gowanus",
                                  "Gravesend",
                                  "Green Point",
                                  "Jamaica Bay", "Kensington", "Madison", "Manhattan Beach", "Marine Park", "Midwood",
                                  "Mall Basin",
                                  "Navy Yard", "Ocean Hill", "Ocean Parkway-North", "Ocean Parkway-South",
                                  "Old Mill Basin",
                                  "Park Slope",
                                  "Park Slope South", "Prospect Heights", "Red Hook", "Seagate", "Sheepshead Bay",
                                  "Spring Creek", "Sunset Park",
                                  "Williamsburg-Central", "Williamsburg-East", "Williamsburg-North",
                                  "Williamsburg-South",
                                  "Windsor Terrace",
                                  "Wyckoff Heights"]
        queens_neighborhoods = ["Airport La Guardia", "Arverne", "Astoria", "Bayside", "Beachhurst", "Belle Harbor",
                                "Bellrose",
                                "Briarwood", "Broad Channel", "Cambria Heights", "College Point", "Corona",
                                "Douglaston",
                                "East Elmhurst",
                                "Elmhurst", "Far Rockaway", "Floral Park", "Flushing Meadow Park", "Flushing-North",
                                "Flushing-South",
                                "Forst Hills", "Fresh Meadows", "Glen Oaks", "Glendale", "Hammels", "Hillcrest",
                                "Hollis",
                                "Hollis Hills",
                                "Holliswood", "Howard Beach", "Jackson Heights", "Jamaica", "Jamaica Bay",
                                "Jamaica Estates", "Jamaica Hills",
                                "Kew Gardens", "Laurelton", "Little Neck", "Long Island City", "Maspeth",
                                "Middle Village",
                                "Neponsit", "Oakland Gardens",
                                "Ozone Park", "Queens Village", "Rego Park", "Richmond Hill", "Ridgewood",
                                "Rockaway Park",
                                "Rosedale",
                                "So. Jamaica-Baisley Park", "South Jamaica", "South Ozone Park", "Springfield Gardens",
                                "St. Albans",
                                "Sunnyside", "Whitestone", "Woodhaven", "Woodside"]
        staten_island_neighborhoods = ["Annadale", "Arden Heights", "Arrochar", "Arrochar-Shore Acres", "Bloomsfield",
                                       "Bulls Head",
                                       "Castleton Corners", "Clove Lakers", "Concord", "Concord-Fox Hills",
                                       "Dongan Hills",
                                       "Dongan Hills-Colony",
                                       "Dongon Hills-Old Town", "Eltingville", "Emerson Hill", "Fresh Kills",
                                       "Grant City",
                                       "Grasmere", "Great Kills",
                                       "Great Kills-Bay Terrace", "Grymes Hill", "Huguenot", "Livingston",
                                       "Manor Heights",
                                       "Mariners Harbor", "Midland Beach",
                                       "New Brighton", "New Brighton-St. George", "New Dorp", "New Dorp-Beach",
                                       "New Dorp-Heights", "New Springfield",
                                       "Oakwood", "Oakwood-Beach", "Pleasant Plains", "Port Ivory", "Port Richmond",
                                       "Princes Bay", "Richmondtown",
                                       "Richmondtown-Lighths Hill", "Rosebank", "Rossville", "Rossville-Charleston",
                                       "Rossville-Port Mobile", "Rossville-Richmond Valley",
                                       "Silver Lake", "South Beach", "Stapleton", "Stapleton-Clifton", "Sunnyside",
                                       "Todt Hill", "Tomkinsville", "Tottenville",
                                       "Travis", "West New Brighton", "Westerleigh", "Willowbrook", "Woodrow"]
        self.neighborhood.set("                         ")
        self.neighborhood_dropdown.destroy()
        if self.borough.get() == "Manhattan":
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, *manhattan_neighborhoods)
        elif self.borough.get() == "The Bronx":
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, *bronx_neighborhoods)
        elif self.borough.get() == "Brooklyn":
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, *brooklyn_neighborhoods)
        elif self.borough.get() == "Queens":
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, *queens_neighborhoods)
        elif self.borough.get() == "Staten Island":
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, *staten_island_neighborhoods)
        else:
            self.neighborhood_dropdown = OptionMenu(self.input_frame, self.neighborhood, "")
        self.neighborhood_dropdown.grid(row=1, column=1, sticky=W)

    # Records all user entered values into a list and pass off to the model
    def getUserValues(self):
        today = date.today()
        current_month = str(today)[5:7]

        # Convert borough to usable form
        if self.borough.get() == "Manhattan":
            new_borough = 1
        elif self.borough.get() == "The Bronx":
            new_borough = 2
        elif self.borough.get() == "Brooklyn":
            new_borough = 3
        elif self.borough.get() == "Queens":
            new_borough = 4
        elif self.borough.get() == "Staten Island":
            new_borough = 5
        else:
            new_borough = ""

        # Convert neighborhood to usable form
        new_neighborhood = self.neighborhood.get().upper()

        # Record the final user data to the user data list
        self.user_data = [new_borough, new_neighborhood, self.building.get(),self.year_entry.get(), self.unit_entry.get(),
                       self.gross_entry.get(), current_month]

        # Close the first window and Start up the Loading Page
        self.master.destroy()
     #   loader = LoadingPage()


# Create a class to give the illusion of the model loading
#class LoadingPage:
 #   def __init__(self):
  #      self.master2 = Tk()
   #     self.master2.title("New York City Price Predictor")

        # Prevent user from changing the window size
    #    self.master2.geometry("350x350")  # Gives a starting geometry to the window
    #    self.master2.resizable(width=False, height=False)

    #    self.time_out()

     #   self.master2.mainloop()

    # A function which will time out and close the loading screen
  #  def time_out(self):
   #     time.sleep(4)
    #    self.master2.destroy()


# Create a class for the user interface detailing the results
class ResultsPage:
    def __init__(self, final_output):
        # Create the master window and its title
        self.results_master = Tk()
        self.results_master.title("New York City Price Predictor")

        # Save the final predicted price to a variable and edit it to later display
        str_final_output = str(final_output)
        # Ensure decimal displays correctly
        decimal_position = str_final_output.find(".")
        if decimal_position == -1:  # AKA no decimal in output
            edited_number = str_final_output + ".00"
        elif (str_final_output[-2] + str_final_output[-1]) == ".0":
            edited_number = str_final_output + "0"
        else:
            edited_number = str_final_output[0: decimal_position + 3]
        # Add commas where appropriate
        full_number = "0" + edited_number[0: decimal_position]
        decimal_number = edited_number[decimal_position:]
        inverted_number = ""
        for i in range(len(full_number) - 1, 0, -1):  # Invert the number to easy add commas
            inverted_number += full_number[i]
        if len(inverted_number) > 3:  # account for prices over $999
            inverted_number = inverted_number[0: 3] + "," + inverted_number[3:]
        if len(inverted_number) > 7:  # account for prices over $999,999
            inverted_number = inverted_number[0: 7] + "," + inverted_number[7:]
        inverted_number = "0" + inverted_number
        final_full_number = ""
        for i in range(len(inverted_number) - 1, 0, -1):  # Undo the Invert
            final_full_number += inverted_number[i]
        # Put the final number to output together
        self.predicted_price = "$" + final_full_number + decimal_number

        # Prevent user from changing the window size
        self.results_master.geometry("600x600")  # Gives a starting geometry to the window
        self.results_master.resizable(width=False, height=False)

        # Create results screen text labels
        self.results_title_label = Label(self.results_master, text="New York City Property Value Predictor", bg="darkblue", fg="white")
        self.results_title_label.config(height=5, width=40)
        self.results_title_label.config(font=("Courier bold", 25))
        self.results_title_label.pack()
        self.results_text_label = Label(self.results_master, text="Your final predicted price is: ")
        self.results_text_label.config(height=5, width=60)
        self.results_text_label.config(font=("Courier", 20))
        self.results_text_label.pack()

        # Display the final predicted price
        self.price_label = Label(self.results_master, text=self.predicted_price, font=("Courier bold", 20))
        self.price_label.pack()

        self.white_space = Label(self.results_master, height=2)
        self.white_space.pack()

        # Create a quit button for when the user is finished
        self.quit_button = Button(self.results_master, text="Quit", command=quit)
        self.quit_button.pack()

        self.results_master.mainloop()