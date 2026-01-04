students = {
    'Alice': {'Attended': 18, 'Total_Classes': 20, 'Assignment': 85},
    'Bob': {'Attended': 15, 'Total_Classes': 20, 'Assignment': 92},
    'Charlie': {'Attended': 20, 'Total_Classes': 20, 'Assignment': 78},
    'Diana': {'Attended': 12, 'Total_Classes': 20, 'Assignment': 95},
    'Eve': {'Attended': 19, 'Total_Classes': 20, 'Assignment': 88}
}

print("original data: ")
for name, attendance in students.items():
    print(f"{name} : {attendance}")
print()

for name in students:
    attendance = students[name]
  
    attendance_percentage = (attendance['Attended'] / attendance['Total_Classes']) * 100
    data = students[name]
    assignment_score = data['Assignment']
    if assignment_score >= 90:
        grade = 'A'
    elif assignment_score >= 80:
        grade = 'B'
    elif assignment_score >= 70:
        grade = 'C'
    elif assignment_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    students[name] = {'Attendance_%': attendance_percentage, 'Grade': grade}
print("After calculating percentage and assignment score:")
for name, data in students.items():
    print(f"{name}: {data}")
print()

# Find student with highest attendance
highest_attendance_student = ""
highest_attendance = 0

for name in students:
    if students[name]['Attendance_%'] > highest_attendance:
        highest_attendance = students[name]['Attendance_%']
        highest_attendance_student = name

print(f"Student with highest attendance: {highest_attendance_student}")
print(f"Attendance percentage: {highest_attendance:.2f}%")
print(f"Grade: {students[highest_attendance_student]['Grade']}\n")

# Find student with highest grade
grader = ""
highest_grade = "F"
grade_order = {"A":5, "B":4, "C":3, "D":2, "F":1}

for name in students:
    current_grade = students[name]['Grade']
    if grade_order[current_grade] > grade_order[highest_grade]:
        highest_grade = current_grade
        grader = name
print(f"Student with highest grade: {grader}")
print(f"{grader} grades is: {highest_grade}\n")

low_attendance_student = []

for name in students:
    if students[name]["Attendance_%"] < 75:
        low_attendance_student.append(name)

print(f"Student with lowest attendance percentage is {low_attendance_student}")

