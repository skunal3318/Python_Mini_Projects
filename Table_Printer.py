#A simple program to print the table of a number by simple interation
print("Table Printer".center(50))

def table():
    num = int(input("Enter the number of which you wan to print the table :: "))

    if num < 0:
        print("Please enter a positive number")
        exit()


    print(f"Table of {num}".center(50))

    print("Number".ljust(10) , "X".ljust(10) , "Table")

    for i in range(1 ,11):
           print(str(num).ljust(10) , "X".ljust(10) , str(i).ljust(10) , "=", str(num*i).ljust(10))

while True:
    table()

    # Ask the user if they want to print another table
    choice = input("Do you want to print another table? (y/n) : ")
    if choice.lower() == 'n':
        print("Thank you for using the table printer")
        break
    elif choice.lower() != 'y':
        print("Please enter a valid choice")
        break



#Thank you for using the table printer