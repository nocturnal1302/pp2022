def get_number(prompt):  # function for inputting number of students or courses
    while True:  # input validation
        try:
            value = int(input(prompt))

        # no error when user input a string, a float, etc
        except ValueError:
            print("Please enter an integer number!")
            continue

        if value <= 0:
            print("Value must be greater than 0.")
            continue
        else:
            break
    return value


def input_number_of_students():
    return get_number('Enter number of students: ')


def add_student(count):
    for i in range(count):
        print(f'Enter information for student {i + 1}:')
        name = input('- Student name: ')
        sid = input('- Student ID: ')
        DoB = input('- Date of Birth: ')

        student = {
            'Name': name,
            'ID': sid,
            'Date of birth': DoB
        }
        students.append(student)
    return students


def input_number_of_courses():
    return get_number('Enter number of courses: ')


def add_course(count):
    for i in range(count):
        print(f'Enter information for course {i+1}:')
        cid = input('- Course ID: ')
        name = input('- Course name: ')

        course = {
            'ID': cid,
            'Name': name
        }
        courses.append(course)
    return courses


def input_mark_for_course():
    # choose from course dict
    pass


def list_student():
    print("\nStudent list")
    for student in students:
        print(f"{student['Name']: <20} {student['ID']: <10} {student['Date of birth']}")


def list_course():
    print("\nCourse list")
    for course in courses:
        print(f"{course['ID']: <10} {course['Name']}")


def show_mark():
    pass


students = []
courses = []

# Enter number of students, info of students, list them
studentCount = input_number_of_students()
add_student(studentCount)
list_student()

# Enter number of courses, info of courses, list them
courseCount = input_number_of_courses()
add_course(courseCount)
list_course()
