#Student Repord Card Generator 
#This program will generate a report card for a student based on their grades and attendance.


# WELCOMING USER
print("Welcome to the Student Report Card Generator".center(50, "-"))


# Taking input from the user to get the marks for each subject
print("Please enter the marks for each subject out of 100".center(50, "-"))
maths = int(input("Enter the marks for Maths: "))
english = int(input("Enter the marks for English: "))
physics = int(input("Enter the marks for Physics: "))
science = int(input("Enter the marks for Science: "))

#Storing marks in a dictionary
my_dict = {
    "Maths": maths,
    "English": english,
    "Physics": physics,
    "Science": science
}

# Calculating total marks and average
total_marks = 0
for subject in my_dict:
    total_marks += my_dict[subject]


average = total_marks / 4



# Displaying the report card
print("Here is the report card for the student:".center(50," "))
print("Subject".ljust(20), "Marks".rjust(10))

for subject in my_dict:
    print(subject.ljust(20), str(my_dict[subject]).rjust(10))


# Displaying total marks and average
print("Total Marks:".ljust(20), str(total_marks).rjust(10))
print("Percentage:".ljust(20), str(average).rjust(10))

# Displaying the grade based on the average
if average >= 90:
    print("Grade : ".ljust(20), "A+".rjust(10))
elif average >= 80:
    print("Grade: ".ljust(20), "A".rjust(10)) 
elif average >= 70:
    print("Grade : ".ljust(20), "B+".rjust(10))
elif average >= 60:
    print("Grade : ".ljust(20), "B".rjust(10))
elif average >= 50:
    print("Grade : ".ljust(20), "C+".rjust(10))
elif average >= 40:
    print("Grade : ".ljust(20), "C".rjust(10))
elif average >= 33:
    print("Grade : ".ljust(20), "D".rjust(10))
else:
    print("Grade : ".ljust(20), "Fail".rjust(10))

# END OF THE PROGRAM
print("Thank you for using the Student Report Card Generator".center(50, "-"))