class Student:
    
    cource = "MCA"
    department = "FOCA"
    
    def __init__(self,rollno, name, contact):
        self.rollno= rollno
        self.name= name
        self.contact= contact

        
    def display(self):
        print("Rollno:", self.rollno)
        print("Name:", self.name)
        print("Contact:", self.contact)
        print("Course:", self.cource)
        print("Contact:", self.department)
        
s1= Student(4112, "Harsh", "0123456789")
s1.display()