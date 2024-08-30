def check_leap_year():
    try:
        # Prompt the user to enter a year
        year = int(input("Enter a year: "))
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:

            print(f"{year} is not a leap year.")
    except ValueError:
        # Handle non-numeric input
        print("Error: Please enter a valid numeric value for the year.")
        # Call the function
check_leap_year()