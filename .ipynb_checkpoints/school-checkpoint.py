class School:
    def __init__(self, name):
        """
        Initializes an object of the class School
        
        Parameters:
        name - str - the name of the school
        """

        self.name = name
        self.courses = {}
        self.students = {}
    
    
    def enroll_student(self, student):
        """
        Adds student to the students dictionary and sets student's school
        
        Parameters:
        student - object - instance of the student class
        """

        self.students.update({student.id:student})
        
        student.set_school(self.name)
    
    
    def remove_student(self, student):
        """
        Removes student from the students dictionary and sets student's school to None
        
        Parameters:
        student - object - instance of the student class
        """

        del self.students[student.id]
        
        student.courses.clear()
        
        student.set_school(None)
    
    
    def add_course(self, course):
        """
        Adds course from the school's course dictionary
        
        Parameters:
        student - object - instance of the student class
        """

        self.courses.update({course.subject:course})
        
    
    def remove_course(self, course):
        """
        Removes course from the school's course dictionary
        
        Parameters:
        student - object - instance of the student class
        """

        del self.courses[course.subject]
        
    
    def kick_student(self, student, course):
        """
        Removes student from a course's roster and remove's course from student's course dictionary
        
        Parameters:
        student - object - instance of the student class
        course - object - instance of the student class
        """

        del course.students[student.id]
        
        del student.courses[course.subject]
    
    
    def __str__(self):
        return self.name
    