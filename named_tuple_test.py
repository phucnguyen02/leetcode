from collections import namedtuple, defaultdict

Employee = namedtuple('Employee', ['position', 'compensation', 'total_office_hours', 'in_office'])
e1 = Employee('SWE', 1000, 10, 10)
print(e1.position)

employee_list = defaultdict(Employee)
employee_list[0] = e1
print(employee_list[0])
print(employee_list[0].compensation)

