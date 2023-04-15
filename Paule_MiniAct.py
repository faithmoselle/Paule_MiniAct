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

print("Mini Act")
print("Rachel Green")
rachelea1 = float(input("Enabling Assessment 1: "))
rachelea2 = float(input("Enabling Assessment 2: "))
rachelea3 = float(input("Enabling Assessment 3: "))
rachelea4 = float(input("Enabling Assessment 4: "))
rachelea5 = float(input("Enabling Assessment 5: "))
rachelsa1 = float(input("Summative Assessment 1: "))
rachelsa2 = float(input("Summative Assessment 2: "))
rachelsa3 = float(input("Summative Assessment 3: "))
rachelfa = float(input("Final Exam: "))

print("\n\nPhoebe Buffay")
phoebeea1 = int(input("Enabling Assessment 1: "))
phoebeea2 = int(input("Enabling Assessment 2: "))
phoebeea3 = int(input("Enabling Assessment 3: "))
phoebeea4 = int(input("Enabling Assessment 4: "))
phoebeea5 = int(input("Enabling Assessment 5: "))
phoebesa1 = int(input("Summative Assessment 1: "))
phoebesa2 = int(input("Summative Assessment 2: "))
phoebesa3 = int(input("Summative Assessment 3: "))
phoebefa = int(input("Final Exam: "))

print("\n\nRoss Geller")
rossea1 = int(input("Enabling Assessment 1: "))
rossea2 = int(input("Enabling Assessment 2: "))
rossea3 = int(input("Enabling Assessment 3: "))
rossea4 = int(input("Enabling Assessment 4: "))
rossea5 = int(input("Enabling Assessment 5: "))
rosssa1 = int(input("Summative Assessment 1: "))
rosssa2 = int(input("Summative Assessment 2: "))
rosssa3 = int(input("Summative Assessment 3: "))
rossfa = int(input("Final Exam: "))

print("\n\nJoey Tribbiani")
joeyea1 = int(input("Enabling Assessment 1: "))
joeyea2 = int(input("Enabling Assessment 2: "))
joeyea3 = int(input("Enabling Assessment 3: "))
joeyea4 = int(input("Enabling Assessment 4: "))
joeyea5 = int(input("Enabling Assessment 5: "))
joeysa1 = int(input("Summative Assessment 1: "))
joeysa2 = int(input("Summative Assessment 2: "))
joeysa3 = int(input("Summative Assessment 3: "))
joeyfa = int(input("Final Exam: "))

print("\n\nChandler Bing")
chandlerea1 = int(input("Enabling Assessment 1: "))
chandlerea2 = int(input("Enabling Assessment 2: "))
chandlerea3 = int(input("Enabling Assessment 3: "))
chandlerea4 = int(input("Enabling Assessment 4: "))
chandlerea5 = int(input("Enabling Assessment 5: "))
chandlersa1 = int(input("Summative Assessment 1: "))
chandlersa2 = int(input("Summative Assessment 2: "))
chandlersa3 = int(input("Summative Assessment 3: "))
chandlerfa = int(input("Final Exam: "))

rachelea = (((rachelea1+rachelea2+rachelea3+rachelea4+rachelea5)/5)*0.3)
rachelsa = (((rachelsa1+rachelsa2+rachelsa3)/3)*0.3)
rachelfe = (rachelfa*0.4)
rachelave = (rachelea+rachelsa+rachelfe)
print("=======================================")
print("Student 1: Rachel Green\nDescription\t\tGrade\tRemark")
print("-----------\t\t-----\t-------")
for rachelremarkea1 in (rachelea1, rachelea2, rachelea3):
    if rachelremarkea1 < 60:
        print("Enabling Assessment\t", format(rachelremarkea1, ".2f"), "\tF")
    elif rachelremarkea1 <= 69:
        print("Enabling Assessment\t", format(rachelremarkea1, ".2f"), "\tD")
    elif rachelremarkea1 <= 79:
        print("Enabling Assessment\t", format(rachelremarkea1, ".2f"), "\tC")
    elif rachelremarkea1 <= 89:
        print("Enabling Assessment\t", format(rachelremarkea1, ".2f"), "\tB")
    elif rachelremarkea1 <= 100:
        print("Enabling Assessment\t", format(rachelremarkea1, ".2f"), "\tA")
for rachelremarkea2 in (rachelea4, rachelea5):
    if rachelremarkea2 < 60:
        print("Enabling Assessment\t", format(rachelremarkea2, ".2f"), "\tF")
    elif rachelremarkea2 <= 69:
        print("Enabling Assessment\t", format(rachelremarkea2, ".2f"), "\tD")
    elif rachelremarkea2 <= 79:
        print("Enabling Assessment\t", format(rachelremarkea2, ".2f"), "\tC")
    elif rachelremarkea2 <= 89:
        print("Enabling Assessment\t", format(rachelremarkea2, ".2f"), "\tB")
    elif rachelremarkea2 <= 100:
        print("Enabling Assessment\t", format(rachelremarkea2, ".2f"), "\tA")
print("---------------------------------------")
for rachelremarksa in (rachelsa1, rachelsa2, rachelsa3):
    if rachelremarksa < 60:
        print("Summative Assessment\t", format(rachelremarksa, ".2f"), "\tF")
    elif rachelremarksa <= 69:
        print("Summative Assessment\t", format(rachelremarksa, ".2f"), "\tD")
    elif rachelremarksa <= 79:
        print("Summative Assessment\t", format(rachelremarksa, ".2f"), "\tC")
    elif rachelremarksa <= 89:
        print("Summative Assessment\t", format(rachelremarksa, ".2f"), "\tB")
    elif rachelremarksa <= 100:
        print("Summative Assessment\t", format(rachelremarksa, ".2f"), "\tA")
print("---------------------------------------")
if rachelfa < 60:
    print("Final Exam\t\t", format(rachelfa, ".2f"), "\tF")
elif rachelfa <= 69:
    print("Final Exam\t\t", format(rachelfa, ".2f"), "\tD")
elif rachelfa <= 79:
    print("Final Exam\t\t", format(rachelfa, ".2f"), "\tC")
elif rachelfa <= 89:
    print("Final Exam\t\t", format(rachelfa, ".2f"), "\tB")
elif rachelfa <= 100:
    print("Final Exam\t\t", format(rachelfa, ".2f"), "\tA")
print("---------------------------------------")
if rachelave < 60:
    print("Average\t\t\t", format(rachelave, ".2f"), "\tF")
elif rachelave <= 69:
    print("Average\t\t\t", format(rachelave, ".2f"), "\tD")
elif rachelave <= 79:
    print("Average\t\t\t", format(rachelave, ".2f"), "\tC")
elif rachelave <= 89:
    print("Average\t\t\t", format(rachelave, ".2f"), "\tB")
elif rachelave <= 100:
    print("Average\t\t\t", format(rachelave, ".2f"), "\tA")
print("=======================================")

# Pheobe
phoebeea = (((phoebeea1+phoebeea2+phoebeea3+phoebeea4+phoebeea5)/5)*0.3)
phoebesa = (((phoebesa1+phoebesa2+phoebesa3)/3)*0.3)
phoebefe = (phoebefa*0.4)
phoebeave = (phoebeea+phoebesa+phoebefe)
print("\n\n=======================================")
print("Student 2: Phoebe Buffay\nDescription\t\tGrade\tRemark")
print("-----------\t\t-----\t-------")
for phoeberemarkea1 in (phoebeea1, phoebeea2, phoebeea3):
    if phoeberemarkea1 < 60:
        print("Enabling Assessment\t", format(phoeberemarkea1, ".2f"), "\tF")
    elif phoeberemarkea1 <= 69:
        print("Enabling Assessment\t", format(phoeberemarkea1, ".2f"), "\tD")
    elif phoeberemarkea1 <= 79:
        print("Enabling Assessment\t", format(phoeberemarkea1, ".2f"), "\tC")
    elif phoeberemarkea1 <= 89:
        print("Enabling Assessment\t", format(phoeberemarkea1, ".2f"), "\tB")
    elif phoeberemarkea1 <= 100:
        print("Enabling Assessment\t", format(phoeberemarkea1, ".2f"), "\tA")
for phoeberemarkea2 in (phoebeea4, phoebeea5):
    if phoeberemarkea2 < 60:
        print("Enabling Assessment\t", format(phoeberemarkea2, ".2f"), "\tF")
    elif phoeberemarkea2 <= 69:
        print("Enabling Assessment\t", format(phoeberemarkea2, ".2f"), "\tD")
    elif phoeberemarkea2 <= 79:
        print("Enabling Assessment\t", format(phoeberemarkea2, ".2f"), "\tC")
    elif phoeberemarkea2 <= 89:
        print("Enabling Assessment\t", format(phoeberemarkea2, ".2f"), "\tB")
    elif phoeberemarkea2 <= 100:
        print("Enabling Assessment\t", format(phoeberemarkea2, ".2f"), "\tA")
print("---------------------------------------")
for phoeberemarksa in (phoebesa1, phoebesa2, phoebesa3):
    if phoeberemarksa < 60:
        print("Summative Assessment\t", format(phoeberemarksa, ".2f"), "\tF")
    elif phoeberemarksa <= 69:
        print("Summative Assessment\t", format(phoeberemarksa, ".2f"), "\tD")
    elif phoeberemarksa <= 79:
        print("Summative Assessment\t", format(phoeberemarksa, ".2f"), "\tC")
    elif phoeberemarksa <= 89:
        print("Summative Assessment\t", format(phoeberemarksa, ".2f"), "\tB")
    elif phoeberemarksa <= 100:
        print("Summative Assessment\t", format(phoeberemarksa, ".2f"), "\tA")
print("---------------------------------------")
if phoebefa < 60:
    print("Final Exam\t\t", format(phoebefa, ".2f"), "\tF")
elif phoebefa <= 69:
    print("Final Exam\t\t", format(phoebefa, ".2f"), "\tD")
elif phoebefa <= 79:
    print("Final Exam\t\t", format(phoebefa, ".2f"), "\tC")
elif phoebefa <= 89:
    print("Final Exam\t\t", format(phoebefa, ".2f"), "\tB")
elif phoebefa <= 100:
    print("Final Exam\t\t", format(phoebefa, ".2f"), "\tA")
print("---------------------------------------")
if phoebeave < 60:
    print("Average\t\t\t", format(phoebeave, ".2f"), "\tF")
elif phoebeave <= 69:
    print("Average\t\t\t", format(phoebeave, ".2f"), "\tD")
elif phoebeave <= 79:
    print("Average\t\t\t", format(phoebeave, ".2f"), "\tC")
elif phoebeave <= 89:
    print("Average\t\t\t", format(phoebeave, ".2f"), "\tB")
elif phoebeave <= 100:
    print("Average\t\t\t", format(phoebeave, ".2f"), "\tA")
print("=======================================")


# Ross
rossea = (((rossea1+rossea2+rossea3+rossea4+rossea5)/5)*0.3)
rosssa = (((rosssa1+rosssa2+rosssa3)/3)*0.3)
rossfe = (rossfa*0.4)
rossave = (rossea+rosssa+rossfe)
print("\n\n=======================================")
print("Student 3: Ross Geller\nDescription\t\tGrade\tRemark")
print("-----------\t\t-----\t-------")
for rossremarkea1 in (rossea1, rossea2, rossea3):
    if rossremarkea1 < 60:
        print("Enabling Assessment\t", format(rossremarkea1, ".2f"), "\tF")
    elif rossremarkea1 <= 69:
        print("Enabling Assessment\t", format(rossremarkea1, ".2f"), "\tD")
    elif rossremarkea1 <= 79:
        print("Enabling Assessment\t", format(rossremarkea1, ".2f"), "\tC")
    elif rossremarkea1 <= 89:
        print("Enabling Assessment\t", format(rossremarkea1, ".2f"), "\tB")
    elif rossremarkea1 <= 100:
        print("Enabling Assessment\t", format(rossremarkea1, ".2f"), "\tA")
for rossremarkea2 in (rossea4, rossea5):
    if rossremarkea2 < 60:
        print("Enabling Assessment\t", format(rossremarkea2, ".2f"), "\tF")
    elif rossremarkea2 <= 69:
        print("Enabling Assessment\t", format(rossremarkea2, ".2f"), "\tD")
    elif rossremarkea2 <= 79:
        print("Enabling Assessment\t", format(rossremarkea2, ".2f"), "\tC")
    elif rossremarkea2 <= 89:
        print("Enabling Assessment\t", format(rossremarkea2, ".2f"), "\tB")
    elif rossremarkea2 <= 100:
        print("Enabling Assessment\t", format(rossremarkea2, ".2f"), "\tA")
print("---------------------------------------")
for rossremarksa in (rosssa1, rosssa2, rosssa3):
    if rossremarksa < 60:
        print("Summative Assessment\t", format(rossremarksa, ".2f"), "\tF")
    elif rossremarksa <= 69:
        print("Summative Assessment\t", format(rossremarksa, ".2f"), "\tD")
    elif rossremarksa <= 79:
        print("Summative Assessment\t", format(rossremarksa, ".2f"), "\tC")
    elif rossremarksa <= 89:
        print("Summative Assessment\t", format(rossremarksa, ".2f"), "\tB")
    elif rossremarksa <= 100:
        print("Summative Assessment\t", format(rossremarksa, ".2f"), "\tA")
print("---------------------------------------")
if rossfa < 60:
    print("Final Exam\t\t", format(rossfa, ".2f"), "\tF")
elif rossfa <= 69:
    print("Final Exam\t\t", format(rossfa, ".2f"), "\tD")
elif rossfa <= 79:
    print("Final Exam\t\t", format(rossfa, ".2f"), "\tC")
elif rossfa <= 89:
    print("Final Exam\t\t", format(rossfa, ".2f"), "\tB")
elif rossfa <= 100:
    print("Final Exam\t\t", format(rossfa, ".2f"), "\tA")
print("---------------------------------------")
if rossave < 60:
    print("Average\t\t\t", format(rossave, ".2f"), "\tF")
elif rossave <= 69:
    print("Average\t\t\t", format(rossave, ".2f"), "\tD")
elif rossave <= 79:
    print("Average\t\t\t", format(rossave, ".2f"), "\tC")
elif rossave <= 89:
    print("Average\t\t\t", format(rossave, ".2f"), "\tB")
elif rossave <= 100:
    print("Average\t\t\t", format(rossave, ".2f"), "\tA")
print("=======================================")


# Joey
joeyea = (((joeyea1+joeyea2+joeyea3+joeyea4+joeyea5)/5)*0.3)
joeysa = (((joeysa1+joeysa2+joeysa3)/3)*0.3)
joeyfe = (joeyfa*0.4)
joeyave = (joeyea+joeysa+joeyfe)
print("\n\n=======================================")
print("Student 4: Joey Tribbiani\nDescription\t\tGrade\tRemark")
print("-----------\t\t-----\t-------")
for joeyremarkea1 in (joeyea1, joeyea2, joeyea3):
    if joeyremarkea1 < 60:
        print("Enabling Assessment\t", format(joeyremarkea1, ".2f"), "\tF")
    elif joeyremarkea1 <= 69:
        print("Enabling Assessment\t", format(joeyremarkea1, ".2f"), "\tD")
    elif joeyremarkea1 <= 79:
        print("Enabling Assessment\t", format(joeyremarkea1, ".2f"), "\tC")
    elif joeyremarkea1 <= 89:
        print("Enabling Assessment\t", format(joeyremarkea1, ".2f"), "\tB")
    elif joeyremarkea1 <= 100:
        print("Enabling Assessment\t", format(joeyremarkea1, ".2f"), "\tA")
for joeyremarkea2 in (joeyea4, joeyea5):
    if joeyremarkea2 < 60:
        print("Enabling Assessment\t", format(joeyremarkea2, ".2f"), "\tF")
    elif joeyremarkea2 <= 69:
        print("Enabling Assessment\t", format(joeyremarkea2, ".2f"), "\tD")
    elif joeyremarkea2 <= 79:
        print("Enabling Assessment\t", format(joeyremarkea2, ".2f"), "\tC")
    elif joeyremarkea2 <= 89:
        print("Enabling Assessment\t", format(joeyremarkea2, ".2f"), "\tB")
    elif joeyremarkea2 <= 100:
        print("Enabling Assessment\t", format(joeyremarkea2, ".2f"), "\tA")
print("---------------------------------------")
for joeyremarksa in (joeysa1, joeysa2, joeysa3):
    if joeyremarksa < 60:
        print("Summative Assessment\t", format(joeyremarksa, ".2f"), "\tF")
    elif joeyremarksa <= 69:
        print("Summative Assessment\t", format(joeyremarksa, ".2f"), "\tD")
    elif joeyremarksa <= 79:
        print("Summative Assessment\t", format(joeyremarksa, ".2f"), "\tC")
    elif joeyremarksa <= 89:
        print("Summative Assessment\t", format(joeyremarksa, ".2f"), "\tB")
    elif joeyremarksa <= 100:
        print("Summative Assessment\t", format(joeyremarksa, ".2f"), "\tA")
print("---------------------------------------")
if joeyfa < 60:
    print("Final Exam\t\t", format(joeyfa, ".2f"), "\tF")
elif joeyfa <= 69:
    print("Final Exam\t\t", format(joeyfa, ".2f"), "\tD")
elif joeyfa <= 79:
    print("Final Exam\t\t", format(joeyfa, ".2f"), "\tC")
elif joeyfa <= 89:
    print("Final Exam\t\t", format(joeyfa, ".2f"), "\tB")
elif joeyfa <= 100:
    print("Final Exam\t\t", format(joeyfa, ".2f"), "\tA")
print("---------------------------------------")
if joeyave < 60:
    print("Average\t\t\t", format(joeyave, ".2f"), "\tF")
elif joeyave <= 69:
    print("Average\t\t\t", format(joeyave, ".2f"), "\tD")
elif joeyave <= 79:
    print("Average\t\t\t", format(joeyave, ".2f"), "\tC")
elif joeyave <= 89:
    print("Average\t\t\t", format(joeyave, ".2f"), "\tB")
elif joeyave <= 100:
    print("Average\t\t\t", format(joeyave, ".2f"), "\tA")
print("=======================================")
chandlerea = (
    ((chandlerea1+chandlerea2+chandlerea3+chandlerea4+chandlerea5)/5)*0.3)
chandlersa = (((chandlersa1+chandlersa2+chandlersa3)/3)*0.3)
chandlerfe = (chandlerfa*0.4)
chandlerave = (chandlerea+chandlersa+chandlerfe)


# Chandler
print("\n\n=======================================")
print("Student 5: Chandler Bing\nDescription\t\tGrade\tRemark")
print("-----------\t\t-----\t-------")
for chandlerremarkea1 in (chandlerea1, chandlerea2, chandlerea3):
    if chandlerremarkea1 < 60:
        print("Enabling Assessment\t", format(chandlerremarkea1, ".2f"), "\tF")
    elif chandlerremarkea1 <= 69:
        print("Enabling Assessment\t", format(chandlerremarkea1, ".2f"), "\tD")
    elif chandlerremarkea1 <= 79:
        print("Enabling Assessment\t", format(chandlerremarkea1, ".2f"), "\tC")
    elif chandlerremarkea1 <= 89:
        print("Enabling Assessment\t", format(chandlerremarkea1, ".2f"), "\tB")
    elif chandlerremarkea1 <= 100:
        print("Enabling Assessment\t", format(chandlerremarkea1, ".2f"), "\tA")
for chandlerremarkea2 in (chandlerea4, chandlerea5):
    if chandlerremarkea2 < 60:
        print("Enabling Assessment\t", format(chandlerremarkea2, ".2f"), "\tF")
    elif chandlerremarkea2 <= 69:
        print("Enabling Assessment\t", format(chandlerremarkea2, ".2f"), "\tD")
    elif chandlerremarkea2 <= 79:
        print("Enabling Assessment\t", format(chandlerremarkea2, ".2f"), "\tC")
    elif chandlerremarkea2 <= 89:
        print("Enabling Assessment\t", format(chandlerremarkea2, ".2f"), "\tB")
    elif chandlerremarkea2 <= 100:
        print("Enabling Assessment\t", format(chandlerremarkea2, ".2f"), "\tA")
print("---------------------------------------")
for chandlerremarksa in (chandlersa1, chandlersa2, chandlersa3):
    if chandlerremarksa < 60:
        print("Summative Assessment\t", format(chandlerremarksa, ".2f"), "\tF")
    elif chandlerremarksa <= 69:
        print("Summative Assessment\t", format(chandlerremarksa, ".2f"), "\tD")
    elif chandlerremarksa <= 79:
        print("Summative Assessment\t", format(chandlerremarksa, ".2f"), "\tC")
    elif chandlerremarksa <= 89:
        print("Summative Assessment\t", format(chandlerremarksa, ".2f"), "\tB")
    elif chandlerremarksa <= 100:
        print("Summative Assessment\t", format(chandlerremarksa, ".2f"), "\tA")
print("---------------------------------------")
if chandlerfa < 60:
    print("Final Exam\t\t", format(chandlerfa, ".2f"), "\tF")
elif chandlerfa <= 69:
    print("Final Exam\t\t", format(chandlerfa, ".2f"), "\tD")
elif chandlerfa <= 79:
    print("Final Exam\t\t", format(chandlerfa, ".2f"), "\tC")
elif chandlerfa <= 89:
    print("Final Exam\t\t", format(chandlerfa, ".2f"), "\tB")
elif chandlerfa <= 100:
    print("Final Exam\t\t", format(chandlerfa, ".2f"), "\tA")
print("---------------------------------------")
if chandlerave < 60:
    print("Average\t\t\t", format(chandlerave, ".2f"), "\tF")
elif chandlerave <= 69:
    print("Average\t\t\t", format(chandlerave, ".2f"), "\tD")
elif chandlerave <= 79:
    print("Average\t\t\t", format(chandlerave, ".2f"), "\tC")
elif chandlerave <= 89:
    print("Average\t\t\t", format(chandlerave, ".2f"), "\tB")
elif chandlerave <= 100:
    print("Average\t\t\t", format(chandlerave, ".2f"), "\tA")
print("=======================================")
