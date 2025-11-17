from Admin_files.Course import Course
def clear_screen():
    for _ in range(50):
        print("\n")

def admin_input_course():
    course_name = input("Enter course name: ")
    time = input("Enter course time (e.g., MWF 10-11AM): ")
    class_list = input("Enter class list (comma separated student names): ").split(",")
    class_list = [student.strip() for student in class_list]
    return Course(course_name, time, class_list)