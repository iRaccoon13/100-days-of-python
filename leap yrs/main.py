##### FUNCTIONS #####

def is_leap_year(yr):
    """Determines if a given year is a leap year."""
    return (yr % 4 == 0) and (not (yr % 100 == 0) or (yr % 400 == 0))

##### Main #####

yrcountinput = input("Would you like to check a single year or multiple? \n 1: Single year \n 2: Multiple years \n")

if yrcountinput == "1":
    startyr = int(input("What year would you like to check? \n"))
    endyr = startyr
elif yrcountinput == "2":
    startyr = int(input("What is the first year you would like to check? \n"))
    endyr = int(input("What is the last year you would like to check? \n"))
else:
    print("Oops!")
    exit(1)

yrdiff = endyr - startyr + 1
yrs = []

for yr in range(startyr, endyr + 1):
    leap = is_leap_year(yr)  # Call the is_leap_year function

    if leap:
        yrs.append(yr)

if yrcountinput == "2":
    print("Leap years:", yrs)
else:
    if leap:
        print(f"{yr} is a leap year!")
    else:
        print(f"{yr} is not a leap year.")
