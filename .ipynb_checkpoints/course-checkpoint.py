class Course:
    def __init__(self, subject):
        """
        Initializes the object of class Course
        
        Parameters:
        subject - str - the class's subject
        """

        self.subject = subject
        self.students = {}
    
    
    def add_student(self, student):
        """
        Adds a student to the students dictionary
        
        Parameters:
        student - object - instance of the Student class
        """

        self.students.update({student.id:student})
        
    
    def remove_student(self, student):
        """
        Removes a student from the students dictionary
        
        Parameters:
        student - object - instance of the Student class
        """
        del self.students[student.id]

    
    def get_subject(self):
        return self.subject
    
    
    def set_subject(self, subject):
        self.subject = subject
        
        
    def __str__(self):
        return self.subject
    