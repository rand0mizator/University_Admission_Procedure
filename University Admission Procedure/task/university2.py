class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.applicants = []
        self.students = []

    def __str__(self):
        return f"\n{self.department_name}"

    def make_applicants(self):
        self.applicants = persons[:]
        self.sort_applicants()
        for applicant in self.applicants:
            if self.department_name in [applicant.department_priorities['First'],
                                        applicant.department_priorities['Second'],
                                        applicant.department_priorities['Third']]:
                self.applicants.append(applicant)
        self.sort_applicants()

    def make_students(self):
        pass

    def sort_applicants(self):
        self.applicants = sorted(self.applicants, key=lambda x: (-int(x.scores[self.department_name]),
                                                                 x.name, x.surname))

    def sort_students(self):
        self.students = sorted(self.students, key=lambda person: (-int(person.scores[self.department_name]),
                                                                  person.name, person.surname))


class Person:
    def __init__(self, person):
        name, surname, phys, chem, math, compsc, dep1, dep2, dep3 = person
        self.name = name
        self.surname = surname
        self.scores = {'Physics': phys,
                       'Chemistry': chem,
                       'Mathematics': math,
                       'Engineering': compsc,
                       'Biotech': chem
                       }
        self.department_priorities = {'First': dep1,
                                      'Second': dep2,
                                      'Third': dep3
                                      }
        self.is_admitted = False


departments_names = ['Physics', 'Chemistry', 'Mathematics', 'Engineering', 'Biotech']

file_name = "applicants.txt"
persons_from_file = []

with open(file_name, 'r') as file:
    for line in file:
        persons_from_file.append(line.split())

maximum_students = int(input())

persons = [Person(person) for person in persons_from_file]
departments = [Department(name) for name in departments_names]


for department in departments:
    print(department)
    for studenter in department.students:
        print(studenter)
