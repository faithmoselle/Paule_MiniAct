''''
    Machine Problem: 
Objective:
Write a Python program that accepts the grades of five students, such as Class participation composed of 5 Enabling Assessment, three (3) Summative Assessment, Final Examination and calculates their grade. The program should display the name of the student, average grade and the corresponding letter grade for each student based on the following grade system:

Formula:
Grade  = (Class participation * 30%) + (Summative Assessment * 30%) + (Final Examination * 40%)

Grade Score	Letter Grade
90 - 100	A
80 - 89	    B
70 - 79	    C
60 - 69	    D
Below 60	F
 
Requirements:

The program should prompt the user to enter the grades of five students.
The program should use a for loop to read the grades of each student using the input
The program should use if-elif-else statements to calculate the letter grade for each student based on the grading system above.
The program should calculate the grade of the five student and display it along with the corresponding letter grade based on the grading system above.
The program should used formatted output to display the results.
Stretch goal: 
Show the result in a table form

Rubrics:
Requirement	Points
Prompts the user to enter the grades of five students	5
Use a for loop to read the grades of each students using input function	5
Use if-elif-else statement to calculate the letter grade for each student based on the grading system	20
Calculate the grade based on the given formula of the students	25
Display the grade and the corresponding letter grade for each student based on the grading system and use the formatted output to display the result	20
Code readability	10
Code efficiency and elegance	5
Stretch Goal	10
Total Machine Problem Grade	100
 

Go to Module Lab SB:
    -copy the url of the home page for your s05/activity repo (URL on browser not the URL from clone button) and link it to our SB lab discussion:
'''
students = {}

for i in range(5):

    name = input(f"\nStudent {i+1}: ")
    cp = 0
    sa = 0
    fe = 0

    # Class Parti
    for classp in range(5):
        cp += float(input("Class participation {}: ".format(classp + 1)))

    # Summative Assessment
    for summa in range(3):
        sa += float(input("Summative assessment {}: ".format(summa + 1)))

    # For Final
    for fexam in range(1):
        fe = float(input("Final exam {}: ".format(fexam + 1)))

    cp = (cp / 5) * 0.3
    sa = (sa / 3) * 0.3
    fe *= 0.4
    ave = cp + sa + fe
    rem = ' '

    if ave >= 90:
        rem = "A"
    elif ave >= 80:
        rem = "B"
    elif ave >= 70:
        rem = "C"
    elif ave >= 60:
        rem = "D"
    else:
        rem = "F"

    students[name] = ave, rem

print("\n")
print(f"{'Student':<15} {'Total Grade':<15} {'Letter Grade':<10}")

for name, grades in students.items():
    ave = grades[0]
    rem = grades[1]
    print(f"{name:<15} {ave:<15.2f} {rem:<10}")
