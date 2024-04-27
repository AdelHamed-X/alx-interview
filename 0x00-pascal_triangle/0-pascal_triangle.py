""" Pascal Triangle Solution using Python """

def pascal_triangle(n):
    """ Pascal Triangle Solution using Python """
    triangle =[]

    for i in range(n):
        if i == 0:
            triangle = [1]
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)

    return triangle

if __name__ == '__main__':
    print(pascal_triangle(5))
