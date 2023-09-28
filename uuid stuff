class Student:
    def __init__(self, name):
        """
        Initializes object of class Student
        
        Parameters:
        name - str - name of student (required)
        grade - int - grade level of the student (required)
        school - str - name of student's school (required)
        """
        from uuid import uuid1

        self.name = name
        
        self.grade = None
        self.courses = {}
        self.school = None
        self.gpa = 4.0
        self.study_count = 0
        
        self.id = uuid1()
    
    
    def study(self):
        self.study_count += 1
        print(f'{self.name} studied for once! HOORAY!')
    
    
    def graduate(self):
        print(f'YAY! {self.name} graduated!')
    
    
    def level_up(self):
        self.grade += 1
        print(f'POGGERS! {self.name} leveled up to grade {self.grade}')
    
    
    def enroll(self, course):
        self.courses.append(course)

        course.add_student(self)

    
    def drop(self, course):
        self.courses.remove(course)
        
        course.remove_student(self)
    
    
    def take_test(self, course):
        if self in course.students.values():
            if self.study_count >= 3:
                print(f"{self.name} passed the test!")

            else:
                print(f"{self.name} failed the test! OH NO!")
                self.gpa -= 0.5

        
    
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
    
if __name__ == '__main__':
    print('I am running directly from the file')
    
