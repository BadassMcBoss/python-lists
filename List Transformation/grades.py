grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

grade_average = sum(grades) / len(grades)
print(grade_average)

passing_grade = 80
grades = ["Failed" if num < passing_grade else num for num in grades]
print(grades)