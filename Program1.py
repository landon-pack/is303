
#Landon Pack IS-303


#Inputs: Student name, Grade for 3 classes, Credits for 3 classes


#Processes: Calculate the GPA using the grades and the credit total


#Outputs: Output the students GPA and report card for student

name = input("What is your name?: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credits: "))
credit2 = int(input("Course 2 credits: "))
credit3 = int(input("Course 3 credits: "))

#Processes: Calculate the GPA using the grades and the credit total

total_credits = credit1 + credit2 + credit3
gpa = ((grade1 * credit1) + (grade2 * credit2) + (grade3 * credit3)) / total_credits

#Outputs: Output the students GPA and report card for student

print(f"{name}'s report card")
print(f"Credits taken: {total_credits}")
print(f"Course 1: Grade {grade1}, Credits: {credit1}\n"
     f"Course 2: Grade {grade2}, Credits: {credit2}\n"
     f"Course 3: Grade {grade3}, Credits: {credit3}")
print(f"GPA: {gpa}")