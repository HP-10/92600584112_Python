class Employee:
    
    # Class variable
    company_Name= 'Cypersoft'
    
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
        
        
    # Instance Method: To get Annual Salary
    def annual_salary(self):
        print(f"{self.name}'s annual salary is: {self.monthly_salary* 12}")
        
    # Class Method: To change company name
    @classmethod
    def change_company(cls, new_name):
        cls.company_Name = new_name
        print(f"Company name changed to :{cls.company_Name}")
        
    # Static Method: To check work day
    @staticmethod
    def isWorkDay(day_name):
        return day_name not in ["Saturday", "Sunday"]
    

print(Employee.isWorkDay("Wednesday"))
print(Employee.isWorkDay("Sunday"))

emp1 = Employee("ABC", 50000)
emp2 = Employee("DEF", 70000)

emp1.annual_salary()
emp2.annual_salary()

Employee.change_company("MegaCorp")
print(emp1.company_Name)
print(emp2.company_Name)