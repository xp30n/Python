name_input = input("What is your first name: ")
age_input = int(input("How old are you: "))

program_input = input("What program are you studying: ")
course_input = int(input("How many courses are you taking: "))
study_input = int(input("Study hours per course: "))

weekly_studies = course_input * study_input

print("--- STUDENT PROFILE ---")
print(f"Name: {name_input}")
print(f"Age: {age_input}")
print(f"Program: {program_input}")
print(f"Courses: {course_input}")
print(f"Weekly study hours: {study_input}")

print(f"Total study hours: {weekly_studies}")

if age_input >= 18:
    print("Adult Confirmed.")
else:
    print("Not an adult.")