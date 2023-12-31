class School:
    def __init__(self, name):

        self.name = name
        self.student_list = []
        #self.years = {}
        self.course_list = []
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    
    def set_student_list(self, new_student):
        self.student_list.append(new_student)
        
    def get_student_list(self):
        return self.student_list
    
    
    def set_course_list(self, course):
        self.course_list.append(course)
        
    def get_course_list(self):
        return self.course_list
    
    
    def enroll_student(self):
        while len(self.student_list) != 3:
            new_student = input("Please enter the name of your student.")
            self.student_list.append(new_student)
    
    def create_course(self):
        courses = ['Math', 'Science', 'History', 'Programming']
        for course in courses:
            self.course_list.append(course)




class Student:
    def __init__(self, name):
        '''
        Defines a student object
        grade_level: current grade/year in school
            example: 9, 10, or 11. As an int
            
        age: age of student
            Displayed as an int
            
        courses: courses student is enrolled in
        school: name of school student attends
        gpa: current gpa of student to determine if they level up, pass, graduate, or fail
        house: subsect of school they belong to
        '''
        from uuid import uuid1

        study_counter = 0
        
        
        self.name = name
        self.grade_level = 
# Create a dict for enrolled/completed for {course : study_count}
        self.enrolled_courses = {}
        self.completed_courses = []
        self.school = 
        self.id = uuid1()
        
# creates a function that will restrieve the name put into the class   
    def get_name(self):
        return self.name
    
# creates a function that allows you to set a name for the object. Important to have getters/setters to avoid wrong data being input   into wrong spot
    def set_name(self, name):
        self.name = name
    
# used when you want to turn the object into a string  
    def __str__(self):
        return self.name
    
    def set_grade_level(self, grade_level):
        self.grade_level = grade_level
        
    def get_grade_level(self):
        return self.grade_level
    
    
        
    def set_school(self, school):
        self.school = school
        
    def get_school(self):
        return self.school
    
    
    
    def set_enrolled_courses():
        self.enrolled_courses.update({course_list_from_school:0})
        
    
    def get_enrolled_courses():
        return self.enrolled_courses
    
    
    def set_completed_courses():
        self.completed_courses = 
    
    def get_completed_courses():
        return self.completed_courses
    
   

# creating student methods, still need to learn to reference other .py files to complete 
    def study():
        study_course = input(f'What course would you like to study for?\n {enrolled_courses.keys()} ')
        enrolled_courses.get(study_course) += 1
        print(f'{self.name} studied. They have studied {enrolled_courses.get(study_course)} times.')
        
# create a graduate function when school is completed, move student from active student to graduated student list
    def graduate():
        
    def level_up():
        self.grade_level += 1
        if self.grade_level > 7:
            graduate():
              
    def enroll_in_course():

    def take_test():
        # (course) needs to be filled in depending on how course/ administer test function operates
        if enrolled_course.get(course) < 4:
            print(f'{self.name} did not pass.')
            enrolled_courses.update(course:0)
            return False
        
        elif enrolled_course.get(course) >= 4:
            print(f'{self.name} passed!')
            completed_courses.append(course)
            enrolled_courses.pop(course)
            return True

            
