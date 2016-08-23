def multiplication_table(row,col):
    output = []
    for n in range(1, row + 1):
        output.append([n * i for i in range(1, col + 1)])
    return output
