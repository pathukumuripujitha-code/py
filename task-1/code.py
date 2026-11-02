


students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = []
    for j in range(3):
        mark = float(input("Enter subject mark: "))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = [name, aggregate, attendance, income]

    students.append(student)

    if (aggregate >= 75 and
        min(subjects) >= 60 and
        attendance >= 75 and
        income <= 200000):

        eligible.append(student)

    else:
        print(name, "is not eligible for scholarship")

# Sort by aggregate, attendance and income
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n----- SCHOLARSHIP RESULTS -----")

if len(eligible) == 0:
    print("No eligible students found")

else:
    print("\nEligible Students Ranking:")

    for i, student in enumerate(eligible, start=1):
        print("\nRank:", i)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])
        print("Status: Scholarship Eligible")

print("\nTotal Eligible Students:", len(eligible))

