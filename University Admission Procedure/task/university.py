file_name = "applicants.txt"
applicants = []

maximum_students = int(input())

with open(file_name, 'r') as file:
    for line in file:
        applicants.append(line.split())

# sorting applicants list by gpa and then alphabeticaly
applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))

departments = {"Biotech": [],
               "Chemistry": [],
               "Engineering": [],
               "Mathematics": [],
               "Physics": []
               }
# creating temporary duplicate of applicants list to track admitted applicants
temp = applicants[:]

# FIRST ROUND of admission, trying to admit student to its FIRST priority department
for applicant in applicants:
    name, surname, gpa, dep1, dep2, dep3 = applicant
    department = dep1
    if len(departments[department]) < maximum_students:
        departments[department].append(applicant)
        temp.remove(applicant)
# coping temp list with removed admitted in FIRST ROUND applicants to initial list of applicants
applicants = temp[:]
# sorting new applicants list by gpa and alphabeticaly
applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))

# SECOND ROUND of admission, trying to admit student to its SECOND priority department
for applicant in applicants:
    name, surname, gpa, dep1, dep2, dep3 = applicant
    department = dep2
    if len(departments[department]) < maximum_students:
        departments[department].append(applicant)
        temp.remove(applicant)
# coping temp list with removed admitted in SECOND ROUND applicants to initial list of applicants
applicants = temp[:]
# sorting new applicants list by gpa and alphabeticaly
applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))

# THIRD ROUND of admission, trying to admit student to its THIRD priority department
for applicant in applicants:
    name, surname, gpa, dep1, dep2, dep3 = applicant
    department = dep3
    if len(departments[department]) < maximum_students:
        departments[department].append(applicant)
        temp.remove(applicant)

# iterating through departments and printing students
for department, students in departments.items():
    print()
    print(department)
    students = sorted(students, key=lambda x: (-float(x[2]), x[0], x[1]))
    for student in students:
        name, surname, gpa, dep1, dep2, dep3 = student
        print(name, surname, gpa)
