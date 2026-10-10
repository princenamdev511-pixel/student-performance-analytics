import pandas as pd
import numpy as np

data = pd.read_csv("students.csv")

print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("--------------------------------------")

print("\nStudent Data:")
print(data.to_string(index=False))

print("\nNumber of Students:", len(data))

print("\nColumns:")
print(list(data.columns))

print("\nBasic Information:")
data.info()

def calculate_total(row):
    total = row["Python"] + row["NumPy"] + row["Pandas"] + row["English"]
    return total

def calculate_average(row):
    marks = np.array([row["Python"], row["NumPy"], row["Pandas"], row["English"]])
    average = np.mean(marks)
    return average

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"

def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

data["Total"] = data.apply(calculate_total, axis=1)
data["Average"] = data.apply(calculate_average, axis=1)
data["Grade"] = data["Average"].apply(calculate_grade)
data["Result"] = data["Average"].apply(check_result)

print("\nStudent Results:")
print(data[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

class_average = np.mean(data["Average"])

highest_average = data["Average"].max()
lowest_average = data["Average"].min()

highest_student = data.loc[data["Average"].idxmax(), "Name"]
lowest_student = data.loc[data["Average"].idxmin(), "Name"]

passed_students = 0
failed_students = 0

for result in data["Result"]:
    if result == "Pass":
        passed_students = passed_students + 1
    else:
        failed_students = failed_students + 1

python_average = np.mean(data["Python"])
numpy_average = np.mean(data["NumPy"])
pandas_average = np.mean(data["Pandas"])
english_average = np.mean(data["English"])

subject_names = ["Python", "NumPy", "Pandas", "English"]
subject_averages = [python_average, numpy_average, pandas_average, english_average]

best_subject = subject_names[0]
best_subject_average = subject_averages[0]

for i in range(len(subject_names)):
    if subject_averages[i] > best_subject_average:
        best_subject = subject_names[i]
        best_subject_average = subject_averages[i]

top_students = data.sort_values("Average", ascending=False).head(3)

print("\nOverall Analysis:")
print("Class Average:", round(class_average, 2))
print("Highest Average:", round(highest_average, 2))
print("Highest Average Student:", highest_student)
print("Lowest Average:", round(lowest_average, 2))
print("Lowest Average Student:", lowest_student)

print("\nPass/Fail:")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

print("\nSubject-wise Average:")
print("Python:", round(python_average, 2))
print("NumPy:", round(numpy_average, 2))
print("Pandas:", round(pandas_average, 2))
print("English:", round(english_average, 2))

print("\nBest Performing Subject:")
print(best_subject, "-", round(best_subject_average, 2))

print("\nTop 3 Students:")
for index, student in top_students.iterrows():
    print(student["Name"], "-", round(student["Average"], 2))