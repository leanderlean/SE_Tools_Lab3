#enrollment system
student_info_list = []

student_name = input("Please input student name: ")
student_age = input("Please input age: ")
student_grade_level = input("What grade level would you like to enroll? ")

if len(student_name.split()) < 2:
    print("Input error: Name must be at least two words.")
else:
    try:
        student_age_int = int(student_age)
        if student_age_int <= 0:
            print("Input error: Age must be a positive integer.")
        else:
            student_info_list.append((f"{student_name}, age: {student_age}, enrolled in grade: {student_grade_level}"))
            print(f"{student_name} is successfully enrolled")
    except ValueError:
        print("Input error: Age must be an integer.")

print(student_info_list)
