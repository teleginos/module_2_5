from typing import List


def get_matrix(n: int, m: int, value: int) -> List:
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


if __name__ == '__main__':
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    print(result1)
    print(result2)
    print(result3)
