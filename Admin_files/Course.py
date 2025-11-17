import random 

class Course: 
    def __init__(self, course_name, time, class_list):
        crns_list = []
        self.course_name = course_name
        CRN = random.randint(10000, 99999)
        if CRN not in crns_list:
            crns_list.append(CRN)
        else:
            while CRN in crns_list:
                CRN = random.randint(10000, 99999)
            crns_list.append(CRN)
        self.CRN = CRN
        self.time = time
        self.class_list = class_list

    def print_course_details(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course ID: {self.course_id}")
        print(f"Time: {self.time}")
        print("Class List:")
        for student in self.class_list:
            print(f"- {student}")
    
    def create_course(self, course_name, time, class_list):
        new_course = Course(course_name, time, class_list)
        return new_course
