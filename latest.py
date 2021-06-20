class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.applicants = []
        self.students = []

    def __str__(self):
        return f"\n{self.department_name}"

    def make_applicants(self, n):
        self.applicants = persons[:]
        self.applicants = self.sort_applicants()
        for applicant in self.applicants:
            if len(self.students) < maximum_students:
                dep = applicant.department_priority[n]
                if dep == self.department_name:
                    applicant.student_of_department = self.department_name
                    applicant.is_admitted = True
                    self.students.append(applicant)
                    # self.applicants.remove(applicant)
        self.students = self.sort_students()
        for person in persons:
            if person in self.students:
                persons.remove(person)

    def sort_applicants(self):
        return sorted(self.applicants, key=lambda applicant: (-applicant.scores[self.department_name],
                                                              applicant.name, applicant.surname))

    def sort_students(self):
        return sorted(self.students, key=lambda student: (-student.scores[self.department_name],
                                                          student.name, student.surname))


class Person:
    def __init__(self, person):
        name, surname, phys, chem, math, compsc, dep1, dep2, dep3 = person
        self.name = name
        self.surname = surname
        self.scores = {'Physics': float(phys),
                       'Chemistry': float(chem),
                       'Mathematics': float(math),
                       'Engineering': float(compsc),
                       'Biotech': float(chem)
                       }
        self.department_priorities = {'First': dep1,
                                      'Second': dep2,
                                      'Third': dep3
                                      }
        self.dep1 = dep1
        self.dep2 = dep2
        self.dep3 = dep3
        self.dep1_score = float(self.scores[self.dep1])
        self.dep2_score = float(self.scores[self.dep2])
        self.dep3_score = float(self.scores[self.dep3])
        self.department_priority = [self.dep1, self.dep2, self.dep3]
        self.is_admitted = False
        self.student_of_department = None

    def __str__(self):
        return f"{self.name} {self.surname} {self.scores[self.student_of_department]}"


departments_names = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']

file_name = "applicants.txt"
persons_from_file = []

with open(file_name, 'r') as file:
    for line in file:
        persons_from_file.append(line.split())

maximum_students = int(input())

persons = [Person(person) for person in persons_from_file]
departments = [Department(name) for name in departments_names]


for department in departments:
    department.make_applicants(0)
    department.make_applicants(1)
    department.make_applicants(2)
    print(department)
    for studenter in department.students:
        print(studenter)
