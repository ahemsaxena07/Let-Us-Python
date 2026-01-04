students = {
    'subu' : {'maths': 88, 'eng': 60, 'sst': 95},
    'amol' : {'maths': 78, 'eng': 68, 'sst': 89},
    'raka' : {'maths': 56, 'eng': 66, 'sst': 77}
}

print("original marks:")
for name, marks in students.items( ):
    print(f"{name} : {marks}")
print()

for name in students:
    marks = students[name]

    marks_list = list(marks.values())
    total = sum(marks_list)
    average = total / len(marks_list)

    students[name] = {'total' : total, 'average': average}

print("after calculating the total and average:")
for name, data in students.items():
    print(f"{name} : {data}")
print()
toppername = " "
highest_total = 0

for name in students:
    if students[name]['total']>highest_total:
        highest_total = students[name]['total']
        toppername = name

print(f"topper of the class: {toppername}")
print(f"total marks: {highest_total}")
print(f"avg marks: {students[toppername]['average']:.2f}")



