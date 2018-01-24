#obtain user input
number_of_students = int(input("Enter the number of students: "))

#init list and sum
scores = []
sum = 0

for student in range(1, number_of_students+1):
    score = int(input("Input score of student number {}: ".format(student)))
    scores.append(score)
    sum += score
print("The scores are:")
print(scores)

#sort in ascending order
scores.sort()

print("Max Score: {}".format(scores[number_of_students-1]))
print("Min Score: {}".format(scores[0]))
print("Average Score: {}".format(sum/number_of_students))
