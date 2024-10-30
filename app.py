import csv

def calculate(csv_file):
    student_scores = {}
    avg = {}
    with open(csv_file, "r") as csv_read:
        header = csv_read.readline().strip().split(",")
        name_index = header.index("Fullname")
        scores_index = header.index("Score")

        for row in csv_read:
            values = row.strip().split(",")

            student_name = values[name_index]
            student_score = int(values[scores_index])

            if student_name in student_scores:
                student_scores[student_name].append(student_score)
            else:
                student_scores[student_name] = [student_score]
            
        for student, score in student_scores.items():
            avg[student] = sum(score) / len(score)
        print(avg)

calculate('text.csv')