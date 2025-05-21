print("""Student Management System
Features:
   Add student
   View all students
   Search by roll number
   Delete student""")


print("Welcome to the Student Management System !!".center(100))
my_dict = {}
while True:
    print("Choose an option from the menu below :: ")
    print("1.Add Student")
    print("2.View All Students")
    print("3.Search By Roll NO. ")
    print("4.Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice : "))
    if choice ==1:
        roll_no = input("Enter roll no. ")
        name = input("Enter name :: ")
        my_dict[roll_no] = name
        print("Student added successfully !!")
    elif  choice == 2:
        print("All Students are :: ")
        for roll_no, name in my_dict.items():
            print(f"Roll No: {roll_no}, Name: {name}") 
         
    elif choice == 3:
        roll_no = input("Enter roll no. to search :: ")
        if roll_no in my_dict:
            print("Student found !!")
            print(my_dict[roll_no])
        else:
            print("Student not found !!")
    elif choice == 4:
        roll_no = input("Enter roll no. to delete :: ")
        if roll_no in my_dict:
            del my_dict[roll_no]
            print("Student deleted successfully !!")
        else:
            print("Student not found !!")

    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break

