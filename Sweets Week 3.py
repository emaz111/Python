number_of_pupils = int(input("Enter the number of pupils: "))
number_of_sweets = int(input("Enter the number of sweets: "))
Pupil_Sweets = number_of_sweets // number_of_pupils
Teacher_Sweets = number_of_sweets % number_of_pupils
print("Each student will get " + str(Pupil_Sweets) + " sweets each. There are " + str(Teacher_Sweets) + " sweets leftover for the teacher")