"""
Student Computer Lab

This program calculates the amount of labs needed relative to the amount of students

The program asks the user to enter the number of students and the number of computers
in each lab, the inputs are stored in their variables. The if statements determines
whether there are enough computers in each lab for the students or not and outputs
the number of labs needed accordingly

"""

Computer_Labs = 0
Count = 1
Students = 0
Computers = 0

while Students <= 0:
    Students = int(input("Enter the number of students: "))
    print("Enter a number greater than zero")

while Computers <=0:
    Computers = int(input("Enter the number of computers in the lab: "))
    print("Enter a number greater than zero")

if Students > Computers:
    Computer_Labs = Students - (Computers % Students)
    while Computer_Labs > 0:
        Computer_Labs = Computer_Labs - Computers
        Count = Count + 1
else:
    Computer_Labs = Computers % Students

if Count >1:
    print("You need " + str(Count) + " labs")
else:
    print("You need 1 lab")

