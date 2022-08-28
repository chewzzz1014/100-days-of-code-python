# key is student name; value is student's score

def get_grade(scores, grades):
    for k, v in scores.items():
        if v <=100 and v>=91:
            grades[k] = "Outstanding"
        elif v <=90 and v>=81:
            grades[k] = "Exceeds Expectations"
        elif v <=80 and v>=71:
            grades[k] = "Acceptable"
        elif v <= 70:
            grades[k] = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

get_grade(student_scores, student_grades)
print(student_grades)
