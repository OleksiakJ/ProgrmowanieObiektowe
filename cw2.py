from typing import List, Any
#zad1 dodawanie macierzy
def sumam(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    temp = []
    for i in range(0, len(A)):
        temp2 = []
        for j in range(0, len(A[i])):
            temp2.append(A[i][j] + B[i][j])

        temp.append(temp2)
    return temp
A: List[List[int]] = [[1,2,3], [4,5,6], [7,8,9]]
B: List[List[int]] = [[4,3,2], [7,5,4], [8,3,5]]

print(sumam(A, B))

#zad 2

# def iloczynm(A: List[List[float]], B: List[List[float]])-> List[List[float]]:
#     temp = []
#     for i in range(0, len(A)):
#         temp2 = []
#         for j in range(0, len(A[i])):
#             x = (A[i][j] * B[i][j]) + (A[i+1][j])
#
#
#     return temp
#
# C: List[List[int]]= [[1,2],
#                        [3,4]]
#
# D: List[List[int]]= [[5,6],
#                        [7,8]]
# print(D[1][0])
# print(iloczynm(C, D))

#zad 3
matrix: List[List[int]] = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
