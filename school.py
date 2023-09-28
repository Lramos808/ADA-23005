class School():
    def __init__(self, name):
        """
        """
        
        self.name = name
        self.courses = list()
        self.students = list()
    
    
    def add_course(self, course):
        self.courses.append(course)
        
        
    def get_courses(self):
        present = 'Courses Available: '
        for x in self.courses:
            present += "\n\t" + x.get_subject()
        return(present)
    
    
    def add_student(self, student):
        self.students.append(student)
        
        
    def get_students(self):
        present = 'Currently Enrolled Students: '
        for x in self.students:
            present += "\n\t" + x.get_name()
        return(present)
    
    
    def remove_student(self, student):
        self.students.remove(student)
    
    
    def get_name(self):
        return(self.name)
    
    
    def set_name(self, name):
        self.name = name
        
        
#     @staticmethod
#     def no_self_required():
#         return "something"