import os
import matplotlib.pyplot as plt


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def loadStudents(fileName):
    file_path = os.path.join(SCRIPT_DIR, fileName)
    with open(file_path, "r") as f:
        students = {}
        for line in f:
            sid, name = line.strip().split(",", 1)
            students[sid] = name
        return students

def loadAssignments(fileName):
    file_path = os.path.join(SCRIPT_DIR, fileName)
    with open(file_path, "r") as f:
        assignments = {}
        for line in f:
            aid, name, points = line.strip().split(",", 2)
            assignments[aid] = (name, float(points))
        return assignments

def loadSubmissions(fileName):
    file_path = os.path.join(SCRIPT_DIR, fileName)
    with open(file_path, "r") as f:
        submissions = []
        for line in f:
            sid, aid, grade = line.strip().split(",")
            submissions.append((sid, aid, float(grade)))
        return submissions


def studentGrade(students, assignments, submissions):
    studentName = input("What is the student's name: ")
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

    students = loadStudents("students.txt")
    assignments = loadAssignments("assignments.txt")
    submissions = loadSubmissions("submissions.txt")


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
    
    
