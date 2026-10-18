class Student:
    
    def __init__(self,rollno, name, contact):
        self.rollno= rollno
        self.name= name
        self.contact= contact 
        
    def display(self):
        print("Rollno:", self.rollno)
        print("Name:", self.name)
        print("Contact:", self.contact)
        
s1= Student(4112, "Harsh", "0123456789")
s1.display()