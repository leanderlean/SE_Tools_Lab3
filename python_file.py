#enrollment system

student_info_list = []

while True:
    student_name = input("Please input student name (or type 'exit' to stop): ")
    if student_name.lower() == 'exit':
        break
    student_age = input("Please input age: ")
    student_grade_level = input("What grade level would you like to enroll? ")
    student_info_list.append((f"{student_name}, age: {student_age}, enrolled in grade: {student_grade_level}"))
    print(f"{student_name} is successfully enrolled")

print(sorted(student_info_list))
