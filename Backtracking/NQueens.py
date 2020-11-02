
def valid_row(placement_cell):
    for i in range(len(placement_cell)-1):
        if placement_cell[i][0] == placement_cell[-1][0]:
            return False
    return True

def valid_col(placement_cell):
    for i in range(len(placement_cell)-1):
        if placement_cell[i][1] == placement_cell[-1][1]:
            return False
    return True

def valid_diag(placement_cell):
    for i in range(len(placement_cell)-1):
        if abs(placement_cell[i][0]-placement_cell[-1][0]) - abs(placement_cell[i][1] - placement_cell[-1][1]) == 0:
            return False
    return True

def is_valid(placement_cell):
    if len(placement_cell) == 1:
        return True
    return valid_row(placement_cell) and valid_col(placement_cell) and valid_diag(placement_cell)

count = [0]
def n_queens_util(n, row, placement_cell):
    if row == n:
        count[0] = count[0] + 1
        print(count[0])
        print(placement_cell)
        placement_cell.pop()
    else:
        for col in range(n):
            placement_cell.append((row, col))
            if is_valid(placement_cell):
                n_queens_util(n, row+1, placement_cell)
            else:
                placement_cell.pop()
        if len(placement_cell) == 0:
            quit()
        placement_cell.pop()

def n_queens(n):
    placement_cell = []
    row = 0
    n_queens_util(n, 0, placement_cell)

n = 12
n_queens(n)



















































# def valid_row(placement_cell):
#     valid = []
#     j = 0
#     for i in range(len(placement_cell)):
#         valid.append(placement_cell[i][j])
#     d = {}
#     for i in valid:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] = d[i] + 1
#     for i in valid:
#         if d[i] > 1:
#             return False
#     return True
#
# def valid_col(placement_cell):
#     valid = []
#     j = 1
#     for i in range(len(placement_cell)):
#         valid.append(placement_cell[i][j])
#     d = {}
#     for i in valid:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] = d[i] + 1
#     for i in valid:
#         if d[i] > 1:
#             return False
#     return True
#
# def valid_diag(placement_cell):
#     row = []
#     col = []
#     j = 0
#     for i in range(len(placement_cell)):
#         row.append(placement_cell[i][j])
#
#     k = 1
#     for i in range(len(placement_cell)):
#         col.append(placement_cell[i][k])
#
#     for i in range(len(placement_cell) - 1):
#         if abs((placement_cell[i][0] - placement_cell[-1][0])) - abs(
#                 (placement_cell[i][1] - placement_cell[-1][1])) == 0:
#             return False
#
#
#     for i in range(len(placement_cell)-2):
#         if abs((placement_cell[i][0] + placement_cell[-1][0])) - abs((placement_cell[i][1] - placement_cell[-1][1])) == 0:
#             return False
#     return True
#
#
# def is_valid(placement_cell):
#     length = len(placement_cell)
#     if length == 1:
#         return True
#     else:
#         return valid_row(placement_cell) and valid_col(placement_cell) and valid_diag(placement_cell)
#
#
#     # row_id = len(placement_cell) - 1
#     # for i in range(0, row_id):
#     #     diff = abs(placement_cell[i] - placement_cell[row_id])
#     #     if diff == 0 or diff == row_id:
#     #         return False
#     # return True
#
# def n_queens_util(n, row, placement_cell, result):
#     count = 0
#     if row == n:
#         result.append(placement_cell)
#         if len(placement_cell) == 0:
#             print("here")
#             quit()
#         placement_cell.pop()
#         print(result[count])
#         count+=1
#     else:
#         for col in range(0, n):
#             placement_cell.append((row,col))
#             # print(placement_cell)
#             if is_valid(placement_cell):
#                 # print(is_valid(placement_cell))
#                 n_queens_util(n, row+1, placement_cell, result)
#             else:
#                 # print(is_valid(placement_cell))
#                 placement_cell.pop()
#         if len(placement_cell) == 0:
#             print("it ends here")
#             quit()
#         placement_cell.pop()
#
#
#
# def n_queens(n):
#     result = []
#     placement_cell = []
#     row = 0
#     n_queens_util(n, row, placement_cell, result)
