
    
# Prompt the user to enter their age
age = int(input("Enter your age: "))
 # Ensure that the age is a positive integer
if age <= 0:
    print("Error: Age must be a positive integer.")

 # Classify the age
if age < 18:
    category = "Minor"
elif age > 65:
    category = "Senior Citizen"
else:
    category = "Adult"
     # Display the category
    print(f"Based on your age, you are classified as: {category}")
  
