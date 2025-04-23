import numpy as np

# Test scores of 5 students across 3 subjects
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Calculate and print the average score for each student
student_average = np.mean(scores, axis=1)
student_avg_roundoff = np.round(student_average, 1)
print("Average score for each student:")
for i, avg in enumerate(student_avg_roundoff):
    print(f"Student {i + 1}: {avg:>5.1f}")

# Calculate and print the average score for each subject
subject_average = np.mean(scores, axis=0)
subject_avg_roundoff = np.round(subject_average, 1)
print("\nAverage score for each subject:")
for i, avg in enumerate(subject_avg_roundoff):
    print(f"Subject {i + 1}: {avg:>5.1f}")

# Identify the student with the highest total score
highest_total_score_index = np.argmax(np.sum(scores, axis=1))
print(f"\nStudent with the highest total score: Student {highest_total_score_index + 1}")
print(f"(row index: {highest_total_score_index})")

# Add 5 bonus points to the third subject for all students
scores[:, 2] += 5
print("\nUpdated scores after adding 5 bonus points to the third subject:")
for row in scores:
    print("".join(f"{score:>5}" for score in row))