grade = int(input("enter a numeric grade between 0 and 100: "))

letter_grade = ""

if grade >= 90 and grade <= 100:
    letter_grade = "A"
elif grade >= 80 and grade <= 89:
    letter_grade = "B"
elif grade >= 70 and grade <= 79:
    letter_grade = "C"
elif grade >= 60 and grade <= 69:
    letter_grade = "D"
elif grade >= 0 and grade < 60:
    letter_grade = "F"
else:
    print("Not a valid number")

if letter_grade != "":
    print("The letter grade is :", letter_grade)
