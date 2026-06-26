student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def convert_to_grades(score):
    
    if score > 90:
        return 'Outstanding'
    elif score > 81:
        return 'Exceeds Expectations'
    elif score > 70:
        return 'Acceptable'
    else:
        return 'Fail'
    
for key in student_scores:
    student_grades[key] = convert_to_grades(student_scores[key])
print(student_grades)
        
        
