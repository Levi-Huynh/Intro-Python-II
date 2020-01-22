
class Dept:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __str__(self):
        return f"Dept: {self.num}: {self.name}"

    def __repr__(self):
        return f'Dept({repr(self.name)}, {repr(self.num)})'

    def find_dept(self, dept_num):
        for d in self.depts:
            if d.num == dept.num:
                return d
        return None  # no object


class Store:
    def __init__(self, name, depts, num):
        self.name = name
        self.depts = depts
        self.num = num

    def __str__(self):
        return f"Store: {self.name}\nDepartments:\n"
        for d in self.depts:
            s += f"  {d.name}\n"

        return s

    def __repr__(self):
        return f'Store({repr(self.name)}, {repr(self.depts)})'

    def find_dept(self, dept_num):
        for d in self.depts:
            if d.num == dept_num:
                return d
        return None


depts = [
    Dept("Dept 1", 11),
    Dept("Dept 2", 13),
    Dept("Dept 3", 33),
]

my_store = Store("Beejs Store", depts, 5)  # create new store object
print(my_store)
print(repr(my_store))

"""
dept_num = int(input("enter dept number: "))
dept = my_store.find_dept(dept_num)
print(dept)
"""