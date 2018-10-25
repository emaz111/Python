number_of_pupils = 16
number_of_sweets = 47
Pupil_Sweets = number_of_sweets // number_of_pupils
Teacher_Sweets = number_of_sweets % number_of_pupils
print("Each student will get " + str(Pupil_Sweets) + " sweets each. There are " + str(Teacher_Sweets) + " sweets leftover for the teacher")