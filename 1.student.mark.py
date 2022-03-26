studentCount = int(input('Enter number of students: '))
if studentCount > 0:
    pass
else:
    print('Number of students must be bigger than 0.')
    quit()

student_list = []
course_list = []

def add_student():
    for i in range(studentCount):
        print(f'Enter information for student {i + 1}:')
        name = input('- Student name: ')
        id = input('- Student ID: ')
        DoB = input('- Date of Birth: ')

        student = (name, id, DoB)  # tuple

        student_list.append(student)  # add tuple as an element to end of list
        print('\n')

def add_course_count():
    pass

def add_course():
    # input course info
    # add to course dict
    pass

def input_mark_for_course():
    # choose from course dict
    pass

def list_course():
    pass

def list_student():
    # for loop
    # loop through list, print student names
    # if empty, prompt to add student
    [print(records) for records in student_list]

def show_mark():
    pass


add_student()
list_student()