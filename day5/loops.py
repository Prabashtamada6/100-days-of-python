student_scores = [12,133,243,12,314,12,1234,1213,13,31,1,3131,3]


max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)