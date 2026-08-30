scores = [45, 88, 72, 91, 55, 60]
passed_scores = []
failed_scores = []

for score in scores:
    if score >= 60:
        passed_scores.append(score)

    else:
        failed_scores.append(score)

print("Passing scores:", passed_scores)
print("Failed Scores", failed_scores)