class Student:
    def __init__(self, name):
        """
        Initializes object of class Student
        
        Parameters:
        name - str - name of student (required)
        """

        from uuid import uuid4

        self.name = name
        self.id = uuid4().hex

        self.grade = None
        self.courses = {}
        self.school = None
        self.gpa = 4.0
    
    
    def enroll(self, course):
        """
        Adds student to course's student list
        Adds course to student's course list
        
        Parameters:
        course - object - instance of Course class
        """

        self.courses.append(course)

        course.add_student(self)

    
    def drop(self, course):
        """
        Removes student from course's student list and vice versa
        
        Parameters:
        course - object - instance of Course class
        """
        del self.courses[course.subject]
        
        course.remove_student(self)
    
    
    def get_name(self):
        return self.name
    
    
    def set_name(self, name):
        self.name = name
    
    
    def get_grade(self):
        return self.grade
    
    
    def set_grade(self, grade):
        self.grade = grade
        
    
    def get_courses(self):
        return self.courses
    
    
    def set_courses(self, courses):
        self.courses = courses
        
    
    def get_school(self):
        return self.school
    
    
    def set_school(self, school):
        self.school = school
        
    
    def get_gpa(self):
        return self.gpa
    
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
       
    def __str__(self):
        return self.name
    