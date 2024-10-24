# Nexabet Toussaint
# 10/20/2024
# Calculate the different placements of grades

'''
BEGIN
CREATE empty list grades_list

FOR module from 1 to 6 DO
PRINT "Enter grade for Module " + module
INPUT grade
ADD grade to grades_list

lowest = MIN(grades_list)
highest = MAX(grades_list)
total = SUM(grades_list)
average = total / 6

PRINT "Lowest grade: " + lowest
PRINT "Highest grade: " + highest
PRINT "Total of grades: " + total
PRINT "Average grade: " + average rounded to 2 decimal places

END
'''

























grades_list = []

# Iterate through the module numbers and collect grades one by one
for module in range(1, 7):
    grade = float(input(f"Enter the grade for Module {module}: "))
    grades_list.append(grade)

# Calculate the lowest grade
lowest_grade = min(grades_list)

# Calculate the highest grade
highest_grade = max(grades_list)

# Calculate the sum of grades
sum_of_grades = sum(grades_list)

# Calculate the average of grades
average_grade = sum_of_grades / len(grades_list)

print("------------Results------------")

# Display the results
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
print("-" * 32)

average_grade = sum(grades_list)/len (grades_list)

# Determine

if average_grade >= 90:
    letter_grade = "A"
elif average_grade >= 80:
    letter_grade = "B"
elif average_grade >= 70:
    letter_grade = "c"
elif average_grade >= 60:
    letter_grade = "D"
elif average_grade >= 59:
    letter_grade = "F"

# Display grade and the average
print(f"Average: {average_grade}    Letter Grade: {letter_grade}")








