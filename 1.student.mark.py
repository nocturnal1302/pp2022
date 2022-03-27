def get_number(prompt):  # function for entering number
    while True:  # input validation
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a positive integer number.")
            continue

        if value <= 0:
            print("Number must be greater than 0")
            continue
        else:
            break
    return value


student_list = []
course_list = []


def input_number_of_student():
    global studentCount
    studentCount = get_number('Enter number of students: ')


def add_student():
    for i in range(studentCount):
        print(f'Enter information for student {i + 1}:')
        name = input('- Student name: ')
        id = input('- Student ID: ')
        DoB = input('- Date of Birth: ')

        student = (name, id, DoB)  # tuple

        student_list.append(student)  # add tuple as an element to end of list
        print('\n')


def input_number_of_courses():
    global courseCount
    courseCount = get_number('Enter number of courses: ')


def add_course():
    for i in range(courseCount):
        print(f'Enter information for course {i + 1}:')
        id = input('- Course ID: ')
        name = input('- Course name: ')

        course = (id, name)

        course_list.append(course)  # add tuple as an element to end of list
        print('\n')


def input_mark_for_course():
    # choose from course dict
    pass


def list_course():
    [print(record) for record in course_list]


def list_student():
    # for loop
    # loop through list, print student names
    [print(record) for record in student_list]


def show_mark():
    pass


input_number_of_student()
add_student()
list_student()

input_number_of_courses()
add_course()
list_course()
