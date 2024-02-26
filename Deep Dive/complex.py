students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

dictionary = []

for i in range(len(students)):
    dictionary.append({
        "student": students[i],
        "grade": grades[i],
        "activity": activities[i]
    })
print(dictionary)

def my_filtering_function(student):
    if student['grade'] > 80:
        return True
    else:
        return False

filtered_grades = filter(my_filtering_function,dictionary)
for d in filtered_grades:
    print(dict(d)['student'])

K = "Status"
append_list = ["Passed", "Passed", "Failed", "Passed"]

dictionary = [{**d, K: v} for d, v in zip(dictionary, append_list)]
print(str(dictionary))