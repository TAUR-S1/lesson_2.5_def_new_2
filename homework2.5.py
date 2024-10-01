def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <=0 or value <= 0:
        return matrix
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
        return matrix

result1 = get_matrix(0 ,2, 10)
print(result1)

