"""The National University conducts an examination of  students in  subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is: Average Score = (Sum of scores obtained by all subjects)/Total no of subjects

Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 """

scores=[]
n, x = map(int, input().split())
for i in range(x):
    scores.append(list(map(float, input().split())))
print(scores)
for student in zip(*scores):
    print(student)
    print(sum(student)/len(student))

#
# a = [20,40,60]
# b = [30,50,70]
# print(zip())
