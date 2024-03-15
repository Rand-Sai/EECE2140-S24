#Test for inclasswork 10
#Mini Project - InClassWork10

#Major dictionary
major_req_dic = {}
major_ele_dic = {}

#Task 1(Multiple Inheritance)
class student:
    def __init__(self, name, major1 = None, major2 = None):
        self.name = name
        self.major1 = major1
        self.major2 = major2

class course:
    def __init__(self, course_name):
        self.course_name = course_name

class reg(student, course):
    def __init__(self, name, course_obj):
        student.__init__(self, name, None)
        course.__init__(self, course_obj.course_name)  # Accessing course_name from course_obj
        self.course_obj = course_obj  # Store the course object
        print("Registering...")
        print(self.name.name + " is registered for " + self.course_obj.course_name)  # Access course_name from course_obj

#Task 2(Single Inheritance)
class major(course):
    def __init__(self, major_name):
        self.major_name = major_name

    #major requirements
    def major_req_add(self, course_obj):
        course.__init__(self, course_obj.course_name)
        self.course_obj = course_obj
        if self.major_name in major_req_dic:
            major_req_dic[self.major_name].append(self.course_obj.course_name)
        else:
            major_req_dic[self.major_name] = [self.course_obj.course_name]
        print(self.course_obj.course_name + " is now a required class for major " + self.major_name)
        print(major_req_dic)

    #check if class in major's requirements
    def major_check_req(self, course_obj):
        course.__init__(self, course_obj.course_name)
        self.course_obj = course_obj
        if self.course_obj.course_name in major_req_dic[self.major_name]:
            print(self.course_obj.course_name + " is a required class for major " + self.major_name)
        else:
            print(self.course_obj.course_name + " is NOT REQUIRED for major " + self.major_name)

#Task 3(Hybrid Inheritance)
class elective(major, course):
    def __init__(self):
        pass
    
    #major electives
    def major_ele_add(self, course_obj):
        course.__init__(self, course_obj.course_name)
        self.course_obj = course_obj
        if self.major_name in major_ele_dic:
            major_ele_dic[self.major_name].append(self.course_obj.course_name)
        else:
            major_ele_dic[self.major_name] = [self.course_obj.course_name]
        print(self.course_obj.course_name + " is now a elective class for major " + self.major_name)
        print(major_ele_dic)

    #check if class in major's electives
    def major_check_ele(self, course_obj):
        course.__init__(self, course_obj.course_name)
        self.course_obj = course_obj
        if self.course_obj.course_name in major_ele_dic[self.major_name]:
            print(self.course_obj.course_name + " is a elective class for major " + self.major_name)
        else:
            print(self.course_obj.course_name + " is NOT AN ELECTIVE for major " + self.major_name)
    

def main():
    #Create course objects
    cour1 = course('EECE2140')
    cour2 = course('EECE2150')
    #Add required classes for each major
    majorEE = major('EE')
    majorEE.major_req_add(cour1)
    majorEE.major_req_add(cour2)
    majorCE = major('CE')
    majorCE.major_req_add(cour1)
    majorCE.major_req_add(cour2)

    #Task 1 Execution
    #stud1 = student('Jack', 'EE')

    #reg1 = reg(stud1, cour1)
    
    #Task 2 Execution
    stud2 = student('Jason', 'EE', 'CE')
    reg2 = reg(stud2, cour2)
    majorEE.major_check_req(cour2)
    majorCE.major_check_req(cour2)

main()
