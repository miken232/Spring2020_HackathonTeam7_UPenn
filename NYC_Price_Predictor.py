import User_Interface
#import nyc_residential_sales

# Create the full welcome page
welcome = User_Interface.WelcomePage()

# Save the user's inputs to a list variable for use in the model
user_information = welcome.user_data
#print(user_information)

#Converting user information to a list to send to "Sale-Predictor model
#Here, user_information list in this order : Borough, Neighborhood, Building class, year built, # of units, GROSS SQ FT, Sale Month
#[1, 'FINANCIAL', '09 COOPS - WALKUP APARTMENTS', '1935', '5', '2019', '01']
# Need to get X_test array from "nyc_residential_sales.py". How?
X_test1=X_test
X_test1=X_test1.drop(X_test1.index[1:])
#print(X_test1)
df = X_test1
#Converting all data values to '0'
df.iloc[0, 0:233] = '0'
#print(df)
X_test1 = df
#print(X_test1). All values must be '0' at this point

#data_sample = (1, 'FINANCIAL', '09 COOPS - WALKUP APARTMENTS', '1935', '5', '2019', '01')
#data_sample_1 = "NEIGHBORHOOD_" + "data_sample[1]"
#print(data_sample_1)

#Updating Column for Residential Units
X_test1.iloc[0, 0] = np.log1p(int(user_information[4]))
#Updating Column for GROSS SQ FT
X_test1.iloc[0, 1] = np.log1p(int(user_information[3]))
#Updating Column for YEAR BUILT
X_test1.iloc[0, 2] = np.log1p(int(user_information[5]))
#print(X_test1)

#Updating Columns for Building Class Category for Col-3 to Col-12
user_information[2] = "BUILDING CLASS CATEGORY_" + user_information[2]
#print(user_information[2])
if user_information[2] == "BUILDING CLASS CATEGORY_04 TAX CLASS 1 CONDOS" :
    X_test1.iloc[0, 3] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_07 RENTALS - WALKUP APARTMENTS" :
    X_test1.iloc[0, 4] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_08 RENTALS - ELEVATOR APARTMENTS" :
    X_test1.iloc[0, 5] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_09 COOPS - WALKUP APARTMENTS" :
    X_test1.iloc[0, 6] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_10 COOPS - ELEVATOR APARTMENTS" :
    X_test1.iloc[0, 7] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_11A CONDO-RENTALS" :
    X_test1.iloc[0, 8] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_12 CONDOS - WALKUP APARTMENTS" :
    X_test1.iloc[0, 9] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_13 CONDOS - ELEVATOR APARTMENTS" :
    X_test1.iloc[0, 10] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_14 RENTALS - 4-10 UNIT" :
    X_test1.iloc[0, 11] = '1'
elif user_information[2] == "BUILDING CLASS CATEGORY_15 CONDOS - 2-10 UNIT RESIDENTIAL" :
    X_test1.iloc[0, 12] = '1'

#Updating Columns for NEIGHBORHOOD for Col-13 to Col-222
user_information[1] = "NEIGHBORHOOD_" + user_information[1]
if user_information[1] == "NEIGHBORHOOD_AIRPORT LA GUARDIA" :
    X_test1.iloc[0, 13] = '1'
elif user_information[1] == "NEIGHBORHOOD_ALPHABET CITY" :
    X_test1.iloc[0, 14] = '1'
elif user_information[1] == "NEIGHBORHOOD_ARDEN HEIGHTS" :
    X_test1.iloc[0, 15] = '1'
elif user_information[1] == "NEIGHBORHOOD_ARROCHAR" :
    X_test1.iloc[0, 16] = '1'
elif user_information[1] == "NEIGHBORHOOD_ARROCHAR-SHORE ACRES" :
    X_test1.iloc[0, 17] = '1'
elif user_information[1] == "NEIGHBORHOOD_ARVERNE" :
    X_test1.iloc[0, 18] = '1'
elif user_information[1] == "NEIGHBORHOOD_ASTORIA" :
    X_test1.iloc[0, 19] = '1'
elif user_information[1] == "NEIGHBORHOOD_BATH BEACH" :
    X_test1.iloc[0, 20] = '1'
elif user_information[1] == "NEIGHBORHOOD_BATHGATE" :
    X_test1.iloc[0, 21] = '1'
elif user_information[1] == "NEIGHBORHOOD_BAY RIDGE" :
    X_test1.iloc[0, 22] = '1'
elif user_information[1] == "NEIGHBORHOOD_BAYCHESTER" :
    X_test1.iloc[0, 23] = '1'
elif user_information[1] == "NEIGHBORHOOD_BAYSIDE" :
    X_test1.iloc[0, 24] = '1'
elif user_information[1] == "NEIGHBORHOOD_BEDFORD PARK/NORWOOD" :
    X_test1.iloc[0, 25] = '1'
elif user_information[1] == "NEIGHBORHOOD_BEDFORD STUYVESANT" :
    X_test1.iloc[0, 26] = '1'
elif user_information[1] == "NEIGHBORHOOD_BEECHHURST" :
    X_test1.iloc[0, 27] = '1'
elif user_information[1] == "NEIGHBORHOOD_BELLE HARBOR" :
    X_test1.iloc[0, 28] = '1'
elif user_information[1] == "NEIGHBORHOOD_BELLEROSE" :
    X_test1.iloc[0, 29] = '1'
elif user_information[1] == "NEIGHBORHOOD_BELMONT" :
    X_test1.iloc[0, 30] = '1'
elif user_information[1] == "NEIGHBORHOOD_BENSONHURST" :
    X_test1.iloc[0, 31] = '1'
elif user_information[1] == "NEIGHBORHOOD_BERGEN BEACH" :
    X_test1.iloc[0, 32] = '1'
elif user_information[1] == "NEIGHBORHOOD_BOERUM HILL" :
    X_test1.iloc[0, 33] = '1'
elif user_information[1] == "NEIGHBORHOOD_BOROUGH PARK" :
    X_test1.iloc[0, 34] = '1'
elif user_information[1] == "NEIGHBORHOOD_BRIARWOOD" :
    X_test1.iloc[0, 35] = '1'
elif user_information[1] == "NEIGHBORHOOD_BRIGHTON BEACH" :
    X_test1.iloc[0, 36] = '1'
elif user_information[1] == "NEIGHBORHOOD_BRONXDALE" :
    X_test1.iloc[0, 37] = '1'
elif user_information[1] == "NEIGHBORHOOD_BROOKLYN HEIGHTS" :
    X_test1.iloc[0, 38] = '1'
elif user_information[1] == "NEIGHBORHOOD_BROWNSVILLE" :
    X_test1.iloc[0, 39] = '1'
elif user_information[1] == "NEIGHBORHOOD_BULLS HEAD" :
    X_test1.iloc[0, 40] = '1'
elif user_information[1] == "NEIGHBORHOOD_BUSH TERMINAL" :
    X_test1.iloc[0, 41] = '1'
elif user_information[1] == "NEIGHBORHOOD_BUSHWICK" :
    X_test1.iloc[0, 42] = '1'
elif user_information[1] == "NEIGHBORHOOD_CANARSIE" :
    X_test1.iloc[0, 43] = '1'
elif user_information[1] == "NEIGHBORHOOD_CARROLL GARDENS" :
    X_test1.iloc[0, 44] = '1'
elif user_information[1] == "NEIGHBORHOOD_CASTLE HILL/UNIONPORT" :
    X_test1.iloc[0, 45] = '1'
elif user_information[1] == "NEIGHBORHOOD_CASTLETON CORNERS" :
    X_test1.iloc[0, 46] = '1'
elif user_information[1] == "NEIGHBORHOOD_CHELSEA" :
    X_test1.iloc[0, 47] = '1'
elif user_information[1] == "NEIGHBORHOOD_CHINATOWN" :
    X_test1.iloc[0, 48] = '1'
elif user_information[1] == "NEIGHBORHOOD_CITY ISLAND" :
    X_test1.iloc[0, 49] = '1'
elif user_information[1] == "NEIGHBORHOOD_CIVIC CENTER" :
    X_test1.iloc[0, 50] = '1'
elif user_information[1] == "NEIGHBORHOOD_CLINTON" :
    X_test1.iloc[0, 51] = '1'
elif user_information[1] == "NEIGHBORHOOD_CLINTON HILL" :
    X_test1.iloc[0, 52] = '1'
elif user_information[1] == "NEIGHBORHOOD_CLOVE LAKES" :
    X_test1.iloc[0, 53] = '1'
elif user_information[1] == "NEIGHBORHOOD_COBBLE HILL" :
    X_test1.iloc[0, 54] = '1'
elif user_information[1] == "NEIGHBORHOOD_COBBLE HILL-WEST" :
    X_test1.iloc[0, 55] = '1'
elif user_information[1] == "NEIGHBORHOOD_COLLEGE POINT" :
    X_test1.iloc[0, 56] = '1'
elif user_information[1] == "NEIGHBORHOOD_CONCORD" :
    X_test1.iloc[0, 57] = '1'
elif user_information[1] == "NEIGHBORHOOD_CONCORD-FOX HILLS" :
    X_test1.iloc[0, 58] = '1'
elif user_information[1] == "NEIGHBORHOOD_CONEY ISLAND" :
    X_test1.iloc[0, 59] = '1'
elif user_information[1] == "NEIGHBORHOOD_CORONA" :
    X_test1.iloc[0, 60] = '1'
elif user_information[1] == "NEIGHBORHOOD_COUNTRY CLUB" :
    X_test1.iloc[0, 61] = '1'
elif user_information[1] == "NEIGHBORHOOD_CROTONA PARK" :
    X_test1.iloc[0, 62] = '1'
elif user_information[1] == "NEIGHBORHOOD_CROWN HEIGHTS" :
    X_test1.iloc[0, 63] = '1'
elif user_information[1] == "NEIGHBORHOOD_CYPRESS HILLS" :
    X_test1.iloc[0, 64] = '1'
elif user_information[1] == "NEIGHBORHOOD_DONGAN HILLS" :
    X_test1.iloc[0, 65] = '1'
elif user_information[1] == "NEIGHBORHOOD_DONGAN HILLS-COLONY" :
    X_test1.iloc[0, 66] = '1'
elif user_information[1] == "NEIGHBORHOOD_DOUGLASTON" :
    X_test1.iloc[0, 67] = '1'
elif user_information[1] == "NEIGHBORHOOD_DOWNTOWN-FULTON FERRY" :
    X_test1.iloc[0, 68] = '1'
elif user_information[1] == "NEIGHBORHOOD_DOWNTOWN-FULTON MALL" :
    X_test1.iloc[0, 69] = '1'
elif user_information[1] == "NEIGHBORHOOD_DOWNTOWN-METROTECH" :
    X_test1.iloc[0, 70] = '1'
elif user_information[1] == "NEIGHBORHOOD_DYKER HEIGHTS" :
    X_test1.iloc[0, 71] = '1'
elif user_information[1] == "NEIGHBORHOOD_EAST ELMHURST" :
    X_test1.iloc[0, 72] = '1'
elif user_information[1] == "NEIGHBORHOOD_EAST NEW YORK" :
    X_test1.iloc[0, 73] = '1'
elif user_information[1] == "NEIGHBORHOOD_EAST TREMONT" :
    X_test1.iloc[0, 74] = '1'
elif user_information[1] == "NEIGHBORHOOD_EAST VILLAGE" :
    X_test1.iloc[0, 75] = '1'
elif user_information[1] == "NEIGHBORHOOD_ELMHURST" :
    X_test1.iloc[0, 76] = '1'
elif user_information[1] == "NEIGHBORHOOD_ELTINGVILLE" :
    X_test1.iloc[0, 77] = '1'
elif user_information[1] == "NEIGHBORHOOD_FAR ROCKAWAY" :
    X_test1.iloc[0, 78] = '1'
elif user_information[1] == "NEIGHBORHOOD_FASHION" :
    X_test1.iloc[0, 79] = '1'
elif user_information[1] == "NEIGHBORHOOD_FINANCIAL" :
    X_test1.iloc[0, 80] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATBUSH-CENTRAL" :
    X_test1.iloc[0, 81] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATBUSH-EAST" :
    X_test1.iloc[0, 82] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATBUSH-LEFFERTS GARDEN" :
    X_test1.iloc[0, 83] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATBUSH-NORTH" :
    X_test1.iloc[0, 84] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATIRON" :
    X_test1.iloc[0, 85] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLATLANDS" :
    X_test1.iloc[0, 86] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLUSHING-NORTH" :
    X_test1.iloc[0, 87] = '1'
elif user_information[1] == "NEIGHBORHOOD_FLUSHING-SOUTH" :
    X_test1.iloc[0, 88] = '1'
elif user_information[1] == "NEIGHBORHOOD_FORDHAM" :
    X_test1.iloc[0, 89] = '1'
elif user_information[1] == "NEIGHBORHOOD_FOREST HILLS" :
    X_test1.iloc[0, 90] = '1'
elif user_information[1] == "NEIGHBORHOOD_FORT GREENE" :
    X_test1.iloc[0, 91] = '1'
elif user_information[1] == "NEIGHBORHOOD_GLENDALE" :
    X_test1.iloc[0, 92] = '1'
elif user_information[1] == "NEIGHBORHOOD_GOWANUS" :
    X_test1.iloc[0, 93] = '1'
elif user_information[1] == "NEIGHBORHOOD_GRAMERCY" :
    X_test1.iloc[0, 94] = '1'
elif user_information[1] == "NEIGHBORHOOD_GRANT CITY" :
    X_test1.iloc[0, 95] = '1'
elif user_information[1] == "NEIGHBORHOOD_GRASMERE" :
    X_test1.iloc[0, 96] = '1'
elif user_information[1] == "NEIGHBORHOOD_GRAVESEND" :
    X_test1.iloc[0, 97] = '1'
elif user_information[1] == "NEIGHBORHOOD_GREAT KILLS" :
    X_test1.iloc[0, 98] = '1'
elif user_information[1] == "NEIGHBORHOOD_GREAT KILLS-BAY TERRACE" :
    X_test1.iloc[0, 99] = '1'
elif user_information[1] == "NEIGHBORHOOD_GREENPOINT" :
    X_test1.iloc[0, 100] = '1'
elif user_information[1] == "NEIGHBORHOOD_GREENWICH VILLAGE-CENTRAL" :
    X_test1.iloc[0, 101] = '1'
elif user_information[1] == "NEIGHBORHOOD_GREENWICH VILLAGE-WEST" :
    X_test1.iloc[0, 102] = '1'
elif user_information[1] == "NEIGHBORHOOD_GRYMES HILL" :
    X_test1.iloc[0, 103] = '1'
elif user_information[1] == "NEIGHBORHOOD_HAMMELS" :
    X_test1.iloc[0, 104] = '1'
elif user_information[1] == "NEIGHBORHOOD_HARLEM-CENTRAL" :
    X_test1.iloc[0, 105] = '1'
elif user_information[1] == "NEIGHBORHOOD_HARLEM-EAST" :
    X_test1.iloc[0, 106] = '1'
elif user_information[1] == "NEIGHBORHOOD_HARLEM-UPPER" :
    X_test1.iloc[0, 107] = '1'
elif user_information[1] == "NEIGHBORHOOD_HARLEM-WEST" :
    X_test1.iloc[0, 108] = '1'
elif user_information[1] == "NEIGHBORHOOD_HIGHBRIDGE/MORRIS HEIGHTS" :
    X_test1.iloc[0, 109] = '1'
elif user_information[1] == "NEIGHBORHOOD_HILLCREST" :
    X_test1.iloc[0, 110] = '1'
elif user_information[1] == "NEIGHBORHOOD_HOLLIS" :
    X_test1.iloc[0, 111] = '1'
elif user_information[1] == "NEIGHBORHOOD_HOWARD BEACH" :
    X_test1.iloc[0, 112] = '1'
elif user_information[1] == "NEIGHBORHOOD_HUNTS POINT" :
    X_test1.iloc[0, 113] = '1'
elif user_information[1] == "NEIGHBORHOOD_INWOOD" :
    X_test1.iloc[0, 114] = '1'
elif user_information[1] == "NEIGHBORHOOD_JACKSON HEIGHTS" :
    X_test1.iloc[0, 115] = '1'
elif user_information[1] == "NEIGHBORHOOD_JAMAICA" :
    X_test1.iloc[0, 116] = '1'
elif user_information[1] == "NEIGHBORHOOD_JAMAICA ESTATES" :
    X_test1.iloc[0, 117] = '1'
elif user_information[1] == "NEIGHBORHOOD_JAVITS CENTER" :
    X_test1.iloc[0, 118] = '1'
elif user_information[1] == "NEIGHBORHOOD_KENSINGTON" :
    X_test1.iloc[0, 119] = '1'
elif user_information[1] == "NEIGHBORHOOD_KEW GARDENS" :
    X_test1.iloc[0, 120] = '1'
elif user_information[1] == "NEIGHBORHOOD_KINGSBRIDGE HTS/UNIV HTS" :
    X_test1.iloc[0, 121] = '1'
elif user_information[1] == "NEIGHBORHOOD_KINGSBRIDGE/JEROME PARK" :
    X_test1.iloc[0, 122] = '1'
elif user_information[1] == "NEIGHBORHOOD_KIPS BAY" :
    X_test1.iloc[0, 123] = '1'
elif user_information[1] == "NEIGHBORHOOD_LAURELTON" :
    X_test1.iloc[0, 124] = '1'
elif user_information[1] == "NEIGHBORHOOD_LITTLE ITALY" :
    X_test1.iloc[0, 125] = '1'
elif user_information[1] == "NEIGHBORHOOD_LITTLE NECK" :
    X_test1.iloc[0, 126] = '1'
elif user_information[1] == "NEIGHBORHOOD_LONG ISLAND CITY" :
    X_test1.iloc[0, 127] = '1'
elif user_information[1] == "NEIGHBORHOOD_LOWER EAST SIDE" :
    X_test1.iloc[0, 128] = '1'
elif user_information[1] == "NEIGHBORHOOD_MADISON" :
    X_test1.iloc[0, 129] = '1'
elif user_information[1] == "NEIGHBORHOOD_MANHATTAN BEACH" :
    X_test1.iloc[0, 130] = '1'
elif user_information[1] == "NEIGHBORHOOD_MANHATTAN VALLEY" :
    X_test1.iloc[0, 131] = '1'
elif user_information[1] == "NEIGHBORHOOD_MARINE PARK" :
    X_test1.iloc[0, 132] = '1'
elif user_information[1] == "NEIGHBORHOOD_MARINERS HARBOR" :
    X_test1.iloc[0, 133] = '1'
elif user_information[1] == "NEIGHBORHOOD_MASPETH" :
    X_test1.iloc[0, 134] = '1'
elif user_information[1] == "NEIGHBORHOOD_MELROSE/CONCOURSE" :
    X_test1.iloc[0, 135] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDDLE VILLAGE" :
    X_test1.iloc[0, 136] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDLAND BEACH" :
    X_test1.iloc[0, 137] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDTOWN CBD" :
    X_test1.iloc[0, 138] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDTOWN EAST" :
    X_test1.iloc[0, 139] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDTOWN WEST" :
    X_test1.iloc[0, 140] = '1'
elif user_information[1] == "NEIGHBORHOOD_MIDWOOD" :
    X_test1.iloc[0, 141] = '1'
elif user_information[1] == "NEIGHBORHOOD_MORRIS PARK/VAN NEST" :
    X_test1.iloc[0, 142] = '1'
elif user_information[1] == "NEIGHBORHOOD_MORRISANIA/LONGWOOD" :
    X_test1.iloc[0, 143] = '1'
elif user_information[1] == "NEIGHBORHOOD_MOTT HAVEN/PORT MORRIS" :
    X_test1.iloc[0, 144] = '1'
elif user_information[1] == "NEIGHBORHOOD_MOUNT HOPE/MOUNT EDEN" :
    X_test1.iloc[0, 145] = '1'
elif user_information[1] == "NEIGHBORHOOD_MURRAY HILL" :
    X_test1.iloc[0, 146] = '1'
elif user_information[1] == "NEIGHBORHOOD_NAVY YARD" :
    X_test1.iloc[0, 147] = '1'
elif user_information[1] == "NEIGHBORHOOD_NEW BRIGHTON" :
    X_test1.iloc[0, 148] = '1'
elif user_information[1] == "NEIGHBORHOOD_NEW BRIGHTON-ST. GEORGE" :
    X_test1.iloc[0, 149] = '1'
elif user_information[1] == "NEIGHBORHOOD_NEW DORP" :
    X_test1.iloc[0, 150] = '1'
elif user_information[1] == "NEIGHBORHOOD_NEW DORP-HEIGHTS" :
    X_test1.iloc[0, 151] = '1'
elif user_information[1] == "NEIGHBORHOOD_NEW SPRINGVILLE" :
    X_test1.iloc[0, 152] = '1'
elif user_information[1] == "NEIGHBORHOOD_OAKLAND GARDENS" :
    X_test1.iloc[0, 153] = '1'
elif user_information[1] == "NEIGHBORHOOD_OCEAN HILL" :
    X_test1.iloc[0, 154] = '1'
elif user_information[1] == "NEIGHBORHOOD_OCEAN PARKWAY-NORTH" :
    X_test1.iloc[0, 155] = '1'
elif user_information[1] == "NEIGHBORHOOD_OCEAN PARKWAY-SOUTH" :
    X_test1.iloc[0, 156] = '1'
elif user_information[1] == "NEIGHBORHOOD_OZONE PARK" :
    X_test1.iloc[0, 157] = '1'
elif user_information[1] == "NEIGHBORHOOD_PARK SLOPE" :
    X_test1.iloc[0, 158] = '1'
elif user_information[1] == "NEIGHBORHOOD_PARK SLOPE SOUTH" :
    X_test1.iloc[0, 159] = '1'
elif user_information[1] == "NEIGHBORHOOD_PARKCHESTER" :
    X_test1.iloc[0, 160] = '1'
elif user_information[1] == "NEIGHBORHOOD_PELHAM PARKWAY NORTH" :
    X_test1.iloc[0, 161] = '1'
elif user_information[1] == "NEIGHBORHOOD_PELHAM PARKWAY SOUTH" :
    X_test1.iloc[0, 162] = '1'
elif user_information[1] == "NEIGHBORHOOD_PORT IVORY" :
    X_test1.iloc[0, 163] = '1'
elif user_information[1] == "NEIGHBORHOOD_PORT RICHMOND" :
    X_test1.iloc[0, 164] = '1'
elif user_information[1] == "NEIGHBORHOOD_PROSPECT HEIGHTS" :
    X_test1.iloc[0, 165] = '1'
elif user_information[1] == "NEIGHBORHOOD_QUEENS VILLAGE" :
    X_test1.iloc[0, 166] = '1'
elif user_information[1] == "NEIGHBORHOOD_RED HOOK" :
    X_test1.iloc[0, 167] = '1'
elif user_information[1] == "NEIGHBORHOOD_REGO PARK" :
    X_test1.iloc[0, 168] = '1'
elif user_information[1] == "NEIGHBORHOOD_RICHMOND HILL" :
    X_test1.iloc[0, 169] = '1'
elif user_information[1] == "NEIGHBORHOOD_RIDGEWOOD" :
    X_test1.iloc[0, 170] = '1'
elif user_information[1] == "NEIGHBORHOOD_RIVERDALE" :
    X_test1.iloc[0, 171] = '1'
elif user_information[1] == "NEIGHBORHOOD_ROCKAWAY PARK" :
    X_test1.iloc[0, 172] = '1'
elif user_information[1] == "NEIGHBORHOOD_ROOSEVELT ISLAND" :
    X_test1.iloc[0, 173] = '1'
elif user_information[1] == "NEIGHBORHOOD_ROSEBANK" :
    X_test1.iloc[0, 174] = '1'
elif user_information[1] == "NEIGHBORHOOD_ROSEDALE" :
    X_test1.iloc[0, 175] = '1'
elif user_information[1] == "NEIGHBORHOOD_ROSSVILLE" :
    X_test1.iloc[0, 176] = '1'
elif user_information[1] == "NEIGHBORHOOD_SCHUYLERVILLE/PELHAM BAY" :
    X_test1.iloc[0, 177] = '1'
elif user_information[1] == "NEIGHBORHOOD_SEAGATE" :
    X_test1.iloc[0, 178] = '1'
elif user_information[1] == "NEIGHBORHOOD_SHEEPSHEAD BAY" :
    X_test1.iloc[0, 179] = '1'
elif user_information[1] == "NEIGHBORHOOD_SILVER LAKE" :
    X_test1.iloc[0, 180] = '1'
elif user_information[1] == "NEIGHBORHOOD_SO. JAMAICA-BAISLEY PARK" :
    X_test1.iloc[0, 181] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOHO" :
    X_test1.iloc[0, 182] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOUNDVIEW" :
    X_test1.iloc[0, 183] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOUTH BEACH" :
    X_test1.iloc[0, 184] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOUTH JAMAICA" :
    X_test1.iloc[0, 185] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOUTH OZONE PARK" :
    X_test1.iloc[0, 186] = '1'
elif user_information[1] == "NEIGHBORHOOD_SOUTHBRIDGE" :
    X_test1.iloc[0, 187] = '1'
elif user_information[1] == "NEIGHBORHOOD_SPRINGFIELD GARDENS" :
    X_test1.iloc[0, 188] = '1'
elif user_information[1] == "NEIGHBORHOOD_ST. ALBANS" :
    X_test1.iloc[0, 189] = '1'
elif user_information[1] == "NEIGHBORHOOD_STAPLETON" :
    X_test1.iloc[0, 190] = '1'
elif user_information[1] == "NEIGHBORHOOD_SUNNYSIDE" :
    X_test1.iloc[0, 191] = '1'
elif user_information[1] == "NEIGHBORHOOD_SUNSET PARK" :
    X_test1.iloc[0, 192] = '1'
elif user_information[1] == "NEIGHBORHOOD_THROGS NECK" :
    X_test1.iloc[0, 193] = '1'
elif user_information[1] == "NEIGHBORHOOD_TOMPKINSVILLE" :
    X_test1.iloc[0, 194] = '1'
elif user_information[1] == "NEIGHBORHOOD_TOTTENVILLE" :
    X_test1.iloc[0, 195] = '1'
elif user_information[1] == "NEIGHBORHOOD_TRAVIS" :
    X_test1.iloc[0, 196] = '1'
elif user_information[1] == "NEIGHBORHOOD_TRIBECA" :
    X_test1.iloc[0, 197] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER EAST SIDE (59-79)" :
    X_test1.iloc[0, 198] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER EAST SIDE (79-96)" :
    X_test1.iloc[0, 199] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER EAST SIDE (96-110)" :
    X_test1.iloc[0, 200] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER WEST SIDE (59-79)" :
    X_test1.iloc[0, 201] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER WEST SIDE (79-96)" :
    X_test1.iloc[0, 202] = '1'
elif user_information[1] == "NEIGHBORHOOD_UPPER WEST SIDE (96-116)" :
    X_test1.iloc[0, 203] = '1'
elif user_information[1] == "NEIGHBORHOOD_WAKEFIELD" :
    X_test1.iloc[0, 204] = '1'
elif user_information[1] == "NEIGHBORHOOD_WASHINGTON HEIGHTS LOWER" :
    X_test1.iloc[0, 205] = '1'
elif user_information[1] == "NEIGHBORHOOD_WASHINGTON HEIGHTS UPPER" :
    X_test1.iloc[0, 206] = '1'
elif user_information[1] == "NEIGHBORHOOD_WEST NEW BRIGHTON" :
    X_test1.iloc[0, 207] = '1'
elif user_information[1] == "NEIGHBORHOOD_WESTCHESTER" :
    X_test1.iloc[0, 208] = '1'
elif user_information[1] == "NEIGHBORHOOD_WESTERLEIGH" :
    X_test1.iloc[0, 209] = '1'
elif user_information[1] == "NEIGHBORHOOD_WHITESTONE" :
    X_test1.iloc[0, 210] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLIAMSBRIDGE" :
    X_test1.iloc[0, 211] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLIAMSBURG-CENTRAL" :
    X_test1.iloc[0, 212] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLIAMSBURG-EAST" :
    X_test1.iloc[0, 213] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLIAMSBURG-NORTH" :
    X_test1.iloc[0, 214] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLIAMSBURG-SOUTH" :
    X_test1.iloc[0, 215] = '1'
elif user_information[1] == "NEIGHBORHOOD_WILLOWBROOK" :
    X_test1.iloc[0, 216] = '1'
elif user_information[1] == "NEIGHBORHOOD_WINDSOR TERRACE" :
    X_test1.iloc[0, 217] = '1'
elif user_information[1] == "NEIGHBORHOOD_WOODHAVEN" :
    X_test1.iloc[0, 218] = '1'
elif user_information[1] == "NEIGHBORHOOD_WOODLAWN" :
    X_test1.iloc[0, 219] = '1'
elif user_information[1] == "NEIGHBORHOOD_WOODSIDE" :
    X_test1.iloc[0, 220] = '1'
elif user_information[1] == "NEIGHBORHOOD_WYCKOFF HEIGHTS" :
    X_test1.iloc[0, 221] = '1'

#Updating Columns for Sale Month for Col-222 to Col-233
user_information[6] = "SALE MONTH_" + user_information[6]
if user_information[6] == "SALE MONTH_01" :
    X_test1.iloc[0, 222] = '1'
elif user_information[6] == "SALE MONTH_02" :
    X_test1.iloc[0, 223] = '1'
elif user_information[6] == "SALE MONTH_03" :
    X_test1.iloc[0, 224] = '1'
elif user_information[6] == "SALE MONTH_04" :
    X_test1.iloc[0, 225] = '1'
elif user_information[6] == "SALE MONTH_05" :
    X_test1.iloc[0, 226] = '1'
elif user_information[6] == "SALE MONTH_06" :
    X_test1.iloc[0, 227] = '1'
elif user_information[6] == "SALE MONTH_07" :
    X_test1.iloc[0, 228] = '1'
elif user_information[6] == "SALE MONTH_08" :
    X_test1.iloc[0, 229] = '1'
elif user_information[6] == "SALE MONTH_09" :
    X_test1.iloc[0, 230] = '1'
elif user_information[6] == "SALE MONTH_10" :
    X_test1.iloc[0, 231] = '1'
elif user_information[6] == "SALE MONTH_11" :
    X_test1.iloc[0, 232] = '1'
elif user_information[6] == "SALE MONTH_12" :
    X_test1.iloc[0, 233] = '1'

Y_pred_test1 = rf_regr.predict(X_test1)
Predictor_Price = (2.71828**(Y_pred_test1)) -1
#print(Y_pred_test1)
#print(Predictor_Price)

# Create the Results Page
#results = User_Interface.ResultsPage(657912.35135135)
results = User_Interface.ResultsPage(Predictor_Price)