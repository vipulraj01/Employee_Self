# Returns a function that creates the Employee class.
class Employee:
    no_of_leaves = 78
    
    # Initialize a new job.
    def __init__(self,name,salary,role):
        self.name = name
        self.salary=salary
        self.role=role
        
    # Returns a human - readable description of the name.
    def printdetaild(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is{self.role}"
    
    # Changes the number of newleaves for this class.
    @classmethod
    def changeleaves(cls,newleaves):
        cls.no_of_leaves = newleaves
        
    # Create a class method from a dash.
    @classmethod
    def fromdash(cls,string):
        return cls(*string.split(","))
    
        
        
# Creates a new Employee object.
harry = Employee("Harry",4500,"Programmer")
rohan = Employee("Rohan",4600,"Salesman")
karan = Employee.fromdash("Karan,6400,teacher")
rahul = Employee.fromdash("rahul,5800,students")

rohan.changeleaves(34)
print(karan.salary)




