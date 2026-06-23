print("***********REPORT CARD SYSTEM**************")

total_marks_obtained = 0

grades = []
subjects = []
marks_list = []

subject = int(input("Enter No. Of Subjects: "))

for i in range(subject):

    subject_name = input("Enter subject name: ")
    marks = int(input("Enter marks: "))

    if marks > 100 or marks < 0:
        print("Invalid marks")
        continue

    # grade calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    # store values
    subjects.append(subject_name)
    marks_list.append(marks)
    grades.append(grade)

    total_marks_obtained += marks


print("\nSubject\t\tMarks\t\tGrade")
print("--------------------------------")

for i in range(subject):
    print(subjects[i], "\t\t", marks_list[i], "\t\t", grades[i])

total_marks_required = subject * 100
percentage = (total_marks_obtained / total_marks_required) * 100

print("\nTotal Marks:", total_marks_required)
print("Total Obtained:", total_marks_obtained)
print("Percentage:", percentage)