# class University:
#     def __init__(self, applicants_from_file, departments_names, max_students=int(input())):
#         self.applicants = [self.Applicant(applicant) for applicant in applicants_from_file]
#         self.departments_names = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
#
#     class Applicant:
#         def __init__(self, applicant):
#             name, surname, phys, chem, math, compsc, dep1, dep2, dep3 = applicant
#             self.name = name
#             self.surname = surname
#             self.phys = phys
#             self.chem = chem
#             self.math = math
#             self.compsc = compsc
#             self.dep1 = dep1
#             self.dep2 = dep2
#             self.dep3 = dep3
#             self.department = None
#
#     class Department:
#         def __init__(self, departments_names):

class Department:
    def __init__(self, department_name, department_exam):
        self.department_name = department_name
        self.department_exam = department_exam
        self.is_full = False
        self.applicants = []
        self.students = []

    def __str__(self):
        return f"{self.department_name} {self.department_exam} {self.is_full} {self.students} {self.applicants}"


class Applicant:
    def __init__(self, applicant):
        name, surname, phys, chem, math, compsc, dep1, dep2, dep3 = applicant
        self.name = name
        self.surname = surname
        self.physics_score = phys
        self.chemistry_score = chem
        self.math_score = math
        self.computer_science_score = compsc
        self.biotech = 0
        self.chemistry = 0
        self.engineering = 0
        self.mathematics = 0
        self.physics = 0
        self.dep1 = dep1
        self.dep2 = dep2
        self.dep3 = dep3
        for dep in [self.dep1, self.dep2, self.dep3]:
            if dep == 'Biotech':
                self.biotech = 1
            elif dep == 'Chemistry':
                self.chemistry = 1
            elif dep == 'Engineering':
                self.engineering = 1
            elif dep == 'Mathematics':
                self.mathematics = 1
            elif dep == 'Physics':
                self.physics = 1
        self.department = None

    def __str__(self):
        return f"{self.name} {self.surname}, physics: {self.physics_score}, chemistry: {self.chemistry_score}, " \
               f"math: {self.math_score}, compsc: {self.computer_science_score}, {self.dep1} {self.dep2} {self.dep3}"


departments_info = {"Biotech": "chemistry",
                    "Chemistry": "chemistry",
                    "Engineering": "computer science",
                    "Mathematics": "math",
                    "Physics": "physics"
                    }

file_name = "applicants.txt"
applicants_from_file = []
applicants = []

with open(file_name, 'r') as file:
    for line in file:
        applicants_from_file.append(line.split())

maximum_students = int(input())

applicants = [Applicant(applicant) for applicant in applicants_from_file]
departments = [Department(name, exam) for name, exam in departments_info.items()]

for applicant in applicants:
    for dep in [applicant.dep1, applicant.dep2, applicant.dep3]:
        for department in departments:
            if dep == department.department_name:
                department.applicants.append(applicant)

for department in departments:
    print(department)
    for applicant in department.applicants:
        print(applicant)
