student_scores = [101, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"Using the function: {max(student_scores)}")

first_score = student_scores[0]

for score in student_scores:
    if score > first_score:
        first_score = score
print(f"Without using the function: {first_score}")

for score in student_scores:
    if score < first_score:
        first_score = score
print(f"The Lowest is: {first_score}")