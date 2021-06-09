maximum_students= int(input())
applicants = []
departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
admissions = {department: [] for department in departments}
# print(admissions)
with open("applicant_list.txt", 'r') as file:
    for line in file:
        applicants.append(line.split())

applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))

for department in departments:
    for applicant in applicants:
        name, surname, gpa, dep1, dep2, dep3 = applicant
        if dep1 == department and len(admissions[department]) < maximum_students:
            admissions[department].append(applicant)
            applicants.remove(applicant)
# print(admissions)
for department, students in admissions.items():
    print()
    print(department)
    for student in students:
        print(f"{student[0]} {student[1]} {student[2]}")




# print(applicants)
# applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))
# print(applicants)

# for applicant in applicants:
#     applicants.remove(applicant)
#     for department in departments:
#         total_admissions = 0
#         print("")
#         print(department)
#         if total_admissions < maximum_students:
#             name, surname, gpa, dep1, dep2, dep3 = applicant
#             if dep1 == department:
#                 total_admissions += 1
#                 print(f"{name} {surname} {gpa}")
#                 continue
#             elif dep2 == department:
#                 total_admissions += 1
#                 print(f"{name} {surname} {gpa}")
#                 continue
#             elif dep3 == department:
#                 total_admissions += 1
#                 print(f"{name} {surname} {gpa}")
#                 continue
#         else:
#             continue
