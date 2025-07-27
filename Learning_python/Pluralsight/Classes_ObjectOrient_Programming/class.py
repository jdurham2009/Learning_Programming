class Employee:
    #Instance Functions (if inside of class = methods)
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    #Needs to be defined to print instances in a readable format or youll get the default output ex: <__main__.Employee object at 0x0000025331EA6BA0>
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"
    
    # Will return an instance as code, that can be evaluated 
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}), "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
    
    #Gets the value, can also be used to set the format of the returned value
    def get_salary(self):
        return self.salary
    
    #Sets a new salary 
    def set_salary(self,salary):
        if salary < 1000:
            raise ValueError("Minimum wage is $1000")
        self.salary = salary


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)