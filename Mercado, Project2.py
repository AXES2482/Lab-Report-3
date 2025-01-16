import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self.name < other.name

    def __ge__(self, other):

        """Returns self >= other, with respect

        to names."""

        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():
    """Tests sorting."""
    num_students = int(input("Enter the number of students: "))
    num_scores = int(input("Enter the number of scores per student: "))

    lyst = []
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        student = Student(name, num_scores)
        for i in range(1, num_scores + 1):
            score = int(input(f"Enter score {i} for {name}: "))
            student.setScore(i, score)
        lyst.append(student)

    # Shuffle list
    random.shuffle(lyst)

    # Display the unsorted list
    print("\nUnsorted list of students:")
    for s in lyst:
        print(s)

    # Sort the list
    lyst.sort()

    # Display the sorted list
    print("\nSorted list of students:")
    for s in lyst:
        print(s)

if __name__ == "__main__":
    main()
