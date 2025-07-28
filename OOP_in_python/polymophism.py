class Employee:

    def __init__(self, name, base_salary, company_name = "ABCcorp"):
        self.name = name
        self.base_salary = base_salary
        self.company_name = company_name

    def calculate_pay(self):
        """To be implemented by subclasses"""
        raise NotImplementedError

    def __str__(self):
        return f"{self.name} from {self.company_name}"


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, base_salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


class CommissionBasedEmployee(Employee):
    def __init__(self, name, project_comission):
        super().__init__(name, base_salary=0)
        self.project_commision = project_comission

    def calculate_pay(self):
        return self.base_salary + self.project_commision


# Using polymorphism
employees = [
    FullTimeEmployee("Alice", base_salary=5000, bonus=1000),
    HourlyEmployee("Bob", hourly_rate=20, hours_worked=120),
    CommissionBasedEmployee("Charlie", project_comission=3000)
]

for emp in employees:
    print(f"{emp}: Pay = ${emp.calculate_pay()}")
