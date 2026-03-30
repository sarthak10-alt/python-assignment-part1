raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("--- Task 1: Profile Cleaning ---")
for student in raw_students:
  #1. Clean the name: strip space and make it Title Case
  clean_name = student["name"].strip().title()
  #2. Clean roll to integer
  clean_roll = int(student["roll"])
  #3. Turn the marks string into a list of actual numbers
  clean_marks = [int(m) for m in student["marks_str"].split(",")]
  #4. Check if name is valid (only letters and spaces)
  is_valid = all(x.isalpha() or x.isspace() for x in clean_name)
  status_icon = "Valid name" if is_valid else "Invalid name"
  print(f"{clean_name}: {status_icon}")

# Store for later
student_info = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
cleaned_students.append(student_info)

#5. Print the profile card
print("-" * 30)
print(f"Student : {clean_name}")
print(f"Roll No : {clean_roll}")
print(f"Marks : {clean_marks}")
print("-" * 30)

# Requirement 4: Print name in ALL CAPS and lowercase for Roll 103
for s in cleaned_students:
  if s["roll"] == 103:
    print(f"Roll 103 Uppercase: {s['name'].upper()}")
    print(f"Roll 103 Lowercase: {s['name'].lower()}")

print("\n--- Task 2: Marks Analysis ---")
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

#1. Grade Label Loop
for i in range(len(subjects)):
  score = marks[i]
  if score >= 90: grade = "A+"
  elif score >= 80: grade = "A"
  elif score >= 70: grade = "B"
  elif score >= 60: grade = "C"
  else: grade = "F"
  print(f"{subjects[i]}: {score} -> Grade: {grade}")

# Calculations
total = sum(marks)
avg = round(total / len(marks), 2)
high_idx = marks.index(max(marks))
low_idx = marks.index(min(marks))

print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")
print(f"Highest: {subjects[high_idx]} ({marks[high_idx]})")
print(f"Lowest: {subjects[low_idx]} ({marks[low_idx]})")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

passed_count = 0 
failed_count = 0
all_averages = []
top_score = -1
topper_name = ""

print(f"{'Name':<15} | {'Average':<8} | {'Status'}")
print("-" * 35)

for name, scores in class_data:
  avg= round(sum(scores) / len(scores), 2)
  status = "Pass" if avg >= 60 else "Fail"

if status == "Pass": passed_count += 1
else: failed_count += 1 

all_averages.append(avg)
if avg > top_score:
  top_score = avg
  topper_name = name

print (f"{name:<15} | {avg:<8} |{status}")

print("-" * 35)
print(f"Students Passed: {passed_count}, Failed: {failed_count}")
print(f"Class Topper: {topper_name} with {top_score}")
print(f"Class Average: {round(sum(all_averages)/len(all_averages), 2)}")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#1. Strip whitespace
clean_essay = essay.strip()
print(f"1. Stripped: '{clean_essay}'")

#2. Title Case
print(f"2. Title Case: {clean_essay.title()}")

#3. Count "python"
count_py = clean_essay.lower().count("python")
print(f"3. 'python' count: {count_py}")

#4. Replace python with Python 
replaced = clean_essay.replace("python", "Python")
print(f"4. Replaced: {replaced}")
#5 & 6. Split into sentences and print numbered 
sentences = [s.strip() for s in clean_essay.split(".") if s.strip()]
print("5/6. Sentences:")
for i, sen in enumerate(sentences, 1):
  if not sen.endswith("."):
    sen += "."
    print(f"{i}. {sen}")
