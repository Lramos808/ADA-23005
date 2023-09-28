class Student:
    def __init__(self, name, year, gpa):
        """
        description of class
        parameters:
            name-str
            age-int
            year- int
            course-list
            school-str
            gpa-float
            house-str
            
        example:
            new_student = Student('Harry Potter', 12, 1, wizardry, 'Hogwarts', 2.0, 'Griffindor')
        """
        
        self.name = name
        self.year = year
        self.courses = list()
        self.school = None
        self.gpa = gpa
        self.study_times = 0
        self.completed = list()
        
        
    def get_name(self):
        return(self.name)
    
    
    def set_name(self, name):
        self.name = name
    
    
    def get_year(self):
        return(self.year)
    
    
    def set_year(self, year):
        self.year = year
    
    
    def get_courses(self):
        present = 'Courses:'
        for x in self.courses:
            present += "\n\t" + x.get_subject()
        return(self.courses)
    
    
    def enroll_course(self, course):
        self.courses.append(course)

        
    def get_school(self):
        return(self.school)
    
    
    def set_school(self, school):
        self.school = school
        
        
    def get_gpa(self):
        return(self.gpa)
    
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
    
    def __str__(self):
        present = str()
        present += "Student Name: " + str(self.name)
        present += "\nYear: " + str(self.year)
        present += "\nEnrolled in: "
        for x in self.courses:
            present += "\n\t" + x.get_subject()
        present += "\nCurrent GPA: "+ str(self.gpa)
        return present
    
    
    def study(self):
        """
        """
        
        print(self.name, "studied like a good student.")
        self.study_times += 1
    
    
    def graduate(self):
        """
        """
        
        print(self.name, "has graduated and is no longer a student.")
        
    
    def level_up(self):
        """
        """
        
        self.year += 1
    
        
    def take_test(self, course, bar):
        """
        """
        
        print(self.name, "has taken a test for:", course)
        if self.study_times > bar:
            print(self.name, "Has Passed the test")
        else:
            print(self.name, "Has Failed the test")
    
if __name__ == '__main__':
    print("Student Class file ran directly")
    
    
    
    ##
    ##