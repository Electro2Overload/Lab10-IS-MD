import os
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_students_path():
    return os.path.join(SCRIPT_DIR, 'data', 'students.txt')

def get_assignments_path():
    return os.path.join(SCRIPT_DIR, 'data', 'assignments.txt')

def get_submissions_path():
    return os.path.join(SCRIPT_DIR, 'data', 'submissions', 'submissions.txt')

def check_file_exists(filePath):
    if not os.path.exists(filePath):
        print(f"Error: {filePath} not found. Make sure the file is uploaded and in the correct directory.")
        return False
    return True

def loadStudents(filePath):
    students = {}
    with open(filePath, "r") as f:
        for line in f:
            line = line.strip()
            student_id = line[:3]
            name = line[3:]
            students[name] = student_id
    return students


def loadAssignments(filePath):
    assignments = {}
    with open(filePath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        for i in range(0, len(lines), 3):
            name = lines[i]
            assignmentID = lines[i + 1]
            pointValue = int(lines[i + 2])
            assignments[name] = {"ID": assignmentID, "points": pointValue}
    return assignments

def loadSubmissions(filePath):
    submissions = []
    with open(filePath, "r") as file:
        for line in file:
            studentID, assignmentID, grade = line.strip().split('|')
            submissions.append((int(studentID), int(assignmentID), int(grade)))
    return submissions


def studentGrade(students, assignments, submissions):
    studentName = input("What is the student's name: ").strip().title()
    if studentName not in students:
        print("Student not found")
        return
    studentID = int(students[studentName])
    totalEarned = 0

    for sub in submissions:
        if sub[0] == studentID:
            for assign in assignments.values():
                if assign["ID"] == str(sub[1]):
                    earned = assign["points"] * (sub[2] / 100)
                    totalEarned += earned
                    break
    maxTotal = sum(assign["points"] for assign in assignments.values())
    finalPercent = round((totalEarned / maxTotal) * 100)
    print(f"{finalPercent}%")


def assignmentStatistics(assignments, submissions):
    assignmentSName = input("What is the assignment name: ").strip()
    if assignmentSName not in assignments:
        print("Assignment not found")
        return
    assignID = assignments[assignmentSName]["ID"]

    scores = [sub[2] for sub in submissions if str(sub[1]) == assignID]

    if not scores:
        print("No submissions found for this assignment.")
        return

    minScore = round(min(scores))
    avgScore = round(sum(scores) / len(scores))
    maxScore = round(max(scores))

    print(f"Min: {minScore}%")
    print(f"Avg: {avgScore}%")
    print(f"Max: {maxScore}%")


def assignmentGraph(assignments, submissions):
    assignmentGName = input("What is the assignment name: ").strip()
    if assignmentGName not in assignments:
        print("Assignment not found")
        return
    assignID = assignments[assignmentGName]["ID"]

    scores = [sub[2] for sub in submissions if str(sub[1]) == assignID]

    if not scores:
        print("No submission found for this assignment.")
        return

    plt.figure(figsize=(8, 6))
    plt.hist(scores, bins=7, edgecolor='black')

    plt.title(f"Scores for {assignmentGName}")
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")

    plt.xlim(45, 100)
    plt.ylim(0, 12)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def main():
    studentsPath = get_students_path()
    assignmentsPath = get_assignments_path()
    submissionsPath = get_submissions_path()
    
    if not (check_file_exists(studentsPath) and check_file_exists(assignmentsPath) and check_file_exists(submissionsPath)):
        return
    
    students = loadStudents(studentsPath)
    assignments = loadAssignments(assignmentsPath)
    submissions = loadSubmissions(submissionsPath)

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("Enter your selection: ").strip()

    if choice == "1":
        studentGrade(students, assignments, submissions)
    elif choice == "2":
        assignmentStatistics(assignments, submissions)
    elif choice == "3":
        assignmentGraph(assignments, submissions)


if __name__ == "__main__":
    main()
