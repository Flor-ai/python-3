def calculate_grade():
    try:
        # Input marks for three subjects
        marks1 = float(input("Enter marks for subject 1 (0-100): "))
        marks2 = float(input("Enter marks for subject 2 (0-100): "))
        marks3 = float(input("Enter marks for subject 3 (0-100): "))
        # Ensure that marks are valid (between 0 and 100)
        if not (0 <= marks1 <= 100) or not (0 <= marks2 <= 100) or not (0 <=marks3 <= 100):
            print("Error: Marks must be between 0 and 100 for each subject.")
        return
        # Calculate the average of the marks
        average = (marks1 + marks2 + marks3) / 3
        # Determine the grade based on the average
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        # Display the calculated grade
        print(f"Your average marks are: {average:.2f}")
        print(f"Your grade is: {grade}")

    except ValueError:
        # Handle non-numeric input
        print("Error: Please enter valid numeric values for the marks.")
        # Call the function
calculate_grade()