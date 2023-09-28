class Course():
    def __init__(self, subject, year, gpa, instructor):
        """
        """
    
        self.subject = subject
        self.year = year
        self.gpa = gpa
        self.instructor = instructor
        self.students = list()
        self.study_bar = 3
        
        
    def get_subject(self):
        return(self.subject)
    
    
    def set_subject(self, subject):
        self.subject = subject
    
    
    def get_year(self):
        return(self.year)
    
    
    def set_year(self, year):
        self.year = year
    
    
    def get_gpa(self):
        return self.gpa
    
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
    
    def get_instructor(self):
        return self.instructor
    
    
    def set_instructor(self, instructor):
        self.instructor = instructor
    
    
    def get_students(self):
        return(self.students)
    
    
    def add_student(self, student):
        self.students.append(student)
        
        
    def remove_student(self, student):
        self.students.remove(student)
        
        
    def __str__(self):
        present = str()
        present += "Course: " + self.subject + " for year: " + str(self.year)
        present += "\nInstructor: " + self.instructor
        present += "\nRoster:" 
        for student in self.students:
            present += "\n\t" + student.get_name()
        return present
    
    
    def administer_test(self):
        for student in self.students:
            student.take_test(self.subject, self.study_bar)
