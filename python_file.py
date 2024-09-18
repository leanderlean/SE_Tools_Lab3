#enrollment system

student_info_list = []
student_name = input("Please input student name: ")
student_age = input("Please input age: ")
student_grade_level = input("What grade level would you like to enroll? ")
student_info_list.append((f"{student_name}, age: {student_age}, enrolled in grade: {student_grade_level}"))
print(f"{student_name} is successfully enrolled")
print(student_info_list)