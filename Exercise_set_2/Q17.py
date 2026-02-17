'''17. Grading of Steel
A certain grade of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are assigned as follows:
• Grade 10: All three conditions are satisfied
• Grade 9: Conditions (i) and (ii) are satisfied
2
• Grade 8: Conditions (ii) and (iii) are satisfied
• Grade 7: Conditions (i) and (iii) are satisfied
• Grade 6: Only one condition is satisfied
• Grade 5: None of the conditions are satisfied
Write a program that takes as input the hardness, carbon content, and tensile strength of
the steel and prints the grade of the steel.'''
hardness = float(input("Enter hardness: "))
carbon_content = float(input("Enter carbon content: "))
tensile_strength = float(input("Enter tensile strength: "))
conditions_met = 0
if hardness > 50:
    conditions_met += 1
if carbon_content < 0.7:
    conditions_met += 1
if tensile_strength > 5600:
    conditions_met += 1
if conditions_met == 3:
    grade = 10
elif conditions_met == 2:
    if hardness > 50 and carbon_content < 0.7:
        grade = 9
    elif carbon_content < 0.7 and tensile_strength > 5600:
        grade = 8
    else:
        grade = 7
elif conditions_met == 1:
    grade = 6
else:
    grade = 5
print(f"The grade of the steel is: {grade}")
