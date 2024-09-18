#enrollment system

student_info_list = []

while True:
    student_name = input("Please input student name (or type 'exit' to stop): ")
    if student_name.lower() == 'exit':
        break

    duplicate_found = False
    for info in student_info_list:
        if student_name.lower() in info.lower():
            duplicate_found = True
            break

    if duplicate_found:
        print(f"Input error: {student_name} is already enrolled.")
        continue

    student_age = input("Please input age: ")
    student_grade_level = input("What grade level would you like to enroll? ")

    if len(student_name.split()) < 2:
        print("Input error: Name must be at least two words.")
        continue

    try:
        student_age_int = int(student_age)
        if student_age_int <= 0:
            print("Input error: Age must be a positive integer.")
            continue
    except ValueError:
        print("Input error: Age must be an integer.")
        continue

    

    student_info_list.append((f"{student_name}, age: {student_age}, enrolled in grade: {student_grade_level}"))
    print(f"{student_name} is successfully enrolled")

print(sorted(student_info_list))


while True:
    student_name = input("Please input student name (or type 'exit' to stop): ")
    if student_name.lower() == 'exit':
        break
    student_age = input("Please input age: ")
    student_grade_level = input("What grade level would you like to enroll? ")
    student_info_list.append((f"{student_name}, age: {student_age}, enrolled in grade: {student_grade_level}"))
    print(f"{student_name} is successfully enrolled")

print(sorted(student_info_list))
